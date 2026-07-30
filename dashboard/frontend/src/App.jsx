import React, { useState, useEffect } from 'react';
import { fetchMetrics, fetchPrices, fetchEvents, fetchChangePoints } from './services/api';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, ReferenceLine } from 'recharts';
import { Activity, Calendar, TrendingDown, DollarSign } from 'lucide-react';

export default function App() {
  const [metrics, setMetrics] = useState({});
  const [prices, setPrices] = useState([]);
  const [events, setEvents] = useState([]);
  const [changePoints, setChangePoints] = useState([]);
  const [startDate, setStartDate] = useState('2013-01-01');
  const [endDate, setEndDate] = useState('2016-12-31');
  const [selectedEvent, setSelectedEvent] = useState(null);

  useEffect(() => {
    fetchMetrics().then(setMetrics);
    fetchEvents().then((res) => setEvents(res.data));
    fetchChangePoints().then((res) => setChangePoints(res.data));
  }, []);

  useEffect(() => {
    fetchPrices(startDate, endDate).then((res) => setPrices(res.data));
  }, [startDate, endDate]);

  return (
    <div className="min-h-screen bg-gray-900 text-gray-100 p-6">
      {/* Header */}
      <header className="mb-8 border-b border-gray-800 pb-4">
        <h1 className="text-3xl font-bold text-blue-400">Brent Crude Oil Analytics Dashboard</h1>
        <p className="text-gray-400 mt-1">
          Interactive Exploration of Historical Trends, Macro Events & Bayesian Change Points
        </p>
      </header>

      {/* Metrics Row */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
        <MetricCard title="Latest Price" value={`$${metrics.latest_price || '--'}`} icon={<DollarSign className="text-green-400" />} />
        <MetricCard title="Historical Avg" value={`$${metrics.avg_price || '--'}`} icon={<Activity className="text-blue-400" />} />
        <MetricCard title="Price Range" value={`$${metrics.min_price || 0} - $${metrics.max_price || 0}`} icon={<TrendingDown className="text-amber-400" />} />
        <MetricCard title="Total Records" value={metrics.total_records || 0} icon={<Calendar className="text-purple-400" />} />
      </div>

      {/* Controls & Date Filter */}
      <div className="bg-gray-800 p-4 rounded-xl mb-6 flex flex-wrap gap-4 items-center justify-between">
        <div className="flex gap-4 items-center">
          <div>
            <label className="block text-xs text-gray-400 mb-1">Start Date</label>
            <input
              type="date"
              value={startDate}
              onChange={(e) => setStartDate(e.target.value)}
              className="bg-gray-700 text-white px-3 py-1.5 rounded border border-gray-600 text-sm"
            />
          </div>
          <div>
            <label className="block text-xs text-gray-400 mb-1">End Date</label>
            <input
              type="date"
              value={endDate}
              onChange={(e) => setEndDate(e.target.value)}
              className="bg-gray-700 text-white px-3 py-1.5 rounded border border-gray-600 text-sm"
            />
          </div>
        </div>

        {/* Event Selector */}
        <div>
          <label className="block text-xs text-gray-400 mb-1">Highlight Event</label>
          <select
            onChange={(e) => setSelectedEvent(events.find(ev => ev.Event_Name === e.target.value))}
            className="bg-gray-700 text-white px-3 py-1.5 rounded border border-gray-600 text-sm"
          >
            <option value="">-- Select Event to Overlay --</option>
            {events.map((ev, i) => (
              <option key={i} value={ev.Event_Name}>
              {ev.Date} - {ev.Event_Name}
              </option>
            ))}
          </select>
        </div>
      </div>

      {/* Main Interactive Chart */}
      <div className="bg-gray-800 p-6 rounded-xl mb-8 shadow-lg">
        <h2 className="text-xl font-semibold mb-4 text-gray-200">Price Trend & Change Point Overlay</h2>
        <div className="h-96">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={prices}>
              <XAxis dataKey="date" stroke="#9CA3AF" tick={{ fontSize: 12 }} />
              <YAxis stroke="#9CA3AF" domain={['auto', 'auto']} />
              <Tooltip contentStyle={{ backgroundColor: '#1F2937', borderColor: '#374151', color: '#fff' }} />
              <Line type="monotone" dataKey="price" stroke="#3B82F6" strokeWidth={2} dot={false} />
              
              {/* Change Point Vertical Line */}
              {changePoints.map((cp, idx) => (
                <ReferenceLine
                  key={idx}
                  x={cp.date}
                  stroke="#EF4444"
                  strokeDasharray="4 4"
                  label={{ value: `Break: ${cp.event_name}`, fill: '#EF4444', position: 'top' }}
                />
              ))}

              {/* Selected Event Line */}
              {selectedEvent && (
                <ReferenceLine
                  x={selectedEvent.Date}
                  stroke="#F59E0B"
                  strokeWidth={2}
                  label={{ value: selectedEvent.Event_Name, fill: '#F59E0B', position: 'insideTopLeft' }}
                />
              )}
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>

      {/* Quantified Change Point Insights Card */}
      {changePoints.length > 0 && (
        <div className="bg-gray-800 p-6 rounded-xl border border-red-500/30">
          <h3 className="text-lg font-bold text-red-400 mb-2">Detected Structural Break Insight</h3>
          <p className="text-gray-300 text-sm">
            On <span className="font-semibold text-white">{changePoints[0].date}</span> ({changePoints[0].event_name}),
            the Bayesian PyMC model identified a structural break where average price dropped from{' '}
            <span className="text-green-400 font-bold">${changePoints[0].pre_mean}</span> to{' '}
            <span className="text-red-400 font-bold">${changePoints[0].post_mean}</span> ({changePoints[0].pct_change}% shift).
          </p>
        </div>
      )}
    </div>
  );
}

function MetricCard({ title, value, icon }) {
  return (
    <div className="bg-gray-800 p-4 rounded-xl flex items-center justify-between border border-gray-700">
      <div>
        <p className="text-xs text-gray-400">{title}</p>
        <p className="text-2xl font-bold text-white mt-1">{value}</p>
      </div>
      <div className="p-3 bg-gray-700/50 rounded-lg">{icon}</div>
    </div>
  );
}