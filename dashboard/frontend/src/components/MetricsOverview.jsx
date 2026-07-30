import React from 'react';

export default function MetricCard({ title, value, icon }) {
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