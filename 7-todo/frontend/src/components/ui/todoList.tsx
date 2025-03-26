import { fetchTodo } from "@/utils/fetch";

function TodoItem({ title, body } : {
    title: string,
    body: string
}) {
    return (
        <article>
            <h3>{title}</h3>
            <p>{body}</p>
        </article>
    );
};

export default async function TodoList() {
    const data: Todo[] = await fetchTodo();
    return (
        <section>
            <h1>Todo List</h1>
            {data.map((todo) => (
                <TodoItem key={ todo.id } title={ todo.title } body={ todo.body } />
            ))}
        </section>
    );
};

type Todo = {
    id: number,
    title: string,
    body: string
};
