import React, { useState, useEffect } from "react";
import axios from "axios";

const CourseList = () => {
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const API_URL = "http://127.0.0.1:8000";

  useEffect(() => {
    fetchCourses();
  }, []);

  const fetchCourses = async () => {
    try {
      setLoading(true);
      const response = await axios.get(API_URL);
      setCourses(response.data);
      setError(null);
    } catch (err) {
      setError("Ошибка загрузки курсов. Попробуйте снова.");
      console.error("Ошибка загрузки курсов:", err);
    } finally {
      setLoading(false);
    }
  };

  if (loading)
    return <div className="text-center mt-5">Загрузка курсов ...</div>;
  if (error) return <div className="alert alert-danger">{error}</div>;

  return (
    <>
      <h1 className="mb-4">Free Online Education</h1>

      {courses.map((course) => (
        <div key={course.id}>
          <p>{course.name}</p>
          <p>{course.description}</p>
        </div>
      ))}
    </>
  );
};

export default CourseList;
