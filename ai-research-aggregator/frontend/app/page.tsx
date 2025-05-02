"use client";
import { useState } from "react";

export default function Home() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    if (!query.trim()) return;

    setLoading(true);
    const response = await fetch("http://localhost:8000/search?query=" + query);


    const data = await response.json();
    setResults(data.results || []);
    setLoading(false);
  };

  return (
    <main className="p-6 max-w-2xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">AI Research Paper Search</h1>

      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Enter keywords like 'machine learning'..."
        className="border border-gray-300 px-4 py-2 w-full rounded mb-4"
      />

      <button
        onClick={handleSearch}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
      >
        {loading ? "Searching..." : "Search"}
      </button>

      <ul className="mt-6 space-y-3">
        {results.map((item, idx) => (
          <li key={idx}>
            <a
              href={item.url}
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-700 underline"
            >
              {item.title}
            </a>
          </li>
        ))}
      </ul>
    </main>
  );
}