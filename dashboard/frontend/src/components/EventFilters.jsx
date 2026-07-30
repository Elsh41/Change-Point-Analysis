import React from 'react';

export default function EventFilters({ startDate, setStartDate, endDate, setEndDate, events, setSelectedEvent }) {
  return (
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

      <div>
        <label className="block text-xs text-gray-400 mb-1">Highlight Event</label>
        <select
          onChange={(e) => setSelectedEvent(events.find(ev => ev.Event_Name === e.target.value))}
          className="bg-gray-700 text-white px-3 py-1.5 rounded border border-gray-600 text-sm"
        >
          <option value="">-- None --</option>
          {events.map((ev, i) => (
            <option key={i} value={ev.Event_Name}>{ev.Date} - {ev.Event_Name}</option>
          ))}
        </select>
      </div>
    </div>
  );
}