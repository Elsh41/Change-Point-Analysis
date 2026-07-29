import axios from 'axios';

const API_BASE = 'http://localhost:5000/api';

export const fetchMetrics = async () => (await axios.get(`${API_BASE}/metrics`)).data;
export const fetchPrices = async (startDate, endDate) => {
  const params = {};
  if (startDate) params.start_date = startDate;
  if (endDate) params.end_date = endDate;
  return (await axios.get(`${API_BASE}/prices`, { params })).data;
};
export const fetchEvents = async () => (await axios.get(`${API_BASE}/events`)).data;
export const fetchChangePoints = async () => (await axios.get(`${API_BASE}/changepoints`)).data;