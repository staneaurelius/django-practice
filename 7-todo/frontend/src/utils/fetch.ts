import axios from "axios";

const api = axios.create({
    baseURL: 'http://localhost:8000/api'
});

async function fetchTodo() {
    try {
        const response = await api.get('/');
        const data = response.data;
        return data;
    } catch(err) {
        console.error('Error:', err);
        throw new Error('Failed to fetch API data');
    };
};

export { fetchTodo };
