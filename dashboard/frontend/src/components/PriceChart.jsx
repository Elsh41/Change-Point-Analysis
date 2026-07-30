import React from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer, ReferenceLine } from 'recharts';

export default function PriceChart({ prices, changePoints, selectedEvent }) {
  return (
    <div className="bg-gray-800 p-6 rounded-xl mb-8 shadow-lg">
      <h2 className="text-xl font-semibold mb-4 text-gray-200">Price Trend & Change Point Overlay</h2>
      <div className="h-96">
        <ResponsiveContainer width="100%" height="100%">
          <LineChart data={prices}>
            <XAxis dataKey="date" stroke="#9CA3AF" tick={{ fontSize: 12 }} />
            <YAxis stroke="#9CA3AF" domain={['auto', 'auto']} />
            <Tooltip contentStyle={{ backgroundColor: '#1F2937', borderColor: '#374151', color: '#fff' }} />
            <Line type="monotone" dataKey="price" stroke="#3B82F6" strokeWidth={2} dot={false} />
            
            {changePoints.map((cp, idx) => (
              <ReferenceLine
                key={idx}
                x={cp.date}
                stroke="#EF4444"
                strokeDasharray="4 4"
                label={{ value: `Break: ${cp.event_name}`, fill: '#EF4444', position: 'top' }}
              />
            ))}

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
  );
}