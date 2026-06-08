"use client";

import { useState } from "react";

export default function DatasetUploader() {

  const [file, setFile] = useState<File | null>(null);

  async function upload() {

    const formData = new FormData();

    formData.append("file", file!);

    await fetch(
      "http://localhost:8000/upload",
      {
        method: "POST",
        body: formData
      }
    );
  }

  return (
    <div className="p-4">

      <input
        type="file"
        onChange={(e) =>
          setFile(e.target.files?.[0] || null)
        }
      />

      <button
        onClick={upload}
        className="bg-blue-500 text-white p-2 rounded"
      >
        Upload Dataset
      </button>

    </div>
  );
}
