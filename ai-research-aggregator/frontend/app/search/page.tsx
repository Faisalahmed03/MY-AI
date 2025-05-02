'use client';

import { useState } from 'react';

export default function SearchPage() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<any[]>([]);

  const handleSearch = async () => {
    if (!query.trim()) return;
    const res = await fetch(`http://127.0.0.1:8000/search?query=${encodeURIComponent(query)}`);
    const data = await res.json();
    setResults(data.results || []);
  };

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Search Research Papers</h1>
      <div className="flex gap-2 mb-4">
        <input
          type="text"
          value={query}
          onChange={e => setQuery(e.target.value)}
          placeholder="Enter search term..."
          className="border p-2 w-full"
        />
        <button onClick={handleSearch} className="bg-blue-600 text-white px-4 py-2 rounded">
          Search
        </button>
      </div>

      <ul>
        {results.map((item, index) => (
          <li key={index} className="mb-2">
            <a href={item.url} target="_blank" rel="noopener noreferrer" className="text-blue-700 underline">
              {item.title}
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
}
