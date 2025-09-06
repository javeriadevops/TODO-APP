import streamlit as st

st.set_page_config(page_title="To-Do List", page_icon="✅", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>✅ Javeria To-Do List App</h1>", unsafe_allow_html=True)
st.write("---")

# Session state for tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# --- Add Task ---
st.subheader("➕ Add a New Task")
new_task = st.text_input("Write your task here:")
if st.button("Add Task"):
    if new_task.strip() != "":
        st.session_state.tasks.append({"task": new_task, "done": False})
        st.success("✅ Task added successfully!")

st.write("---")
st.subheader("📋 Your Tasks")

# --- Show Tasks ---
if st.session_state.tasks:
    for i, t in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([0.1, 0.75, 0.15])
        
        # Checkbox for marking done
        with col1:
            done = st.checkbox("", value=t["done"], key=f"task_{i}")
            st.session_state.tasks[i]["done"] = done
        
        # Task text styled
        with col2:
            if t["done"]:
                st.markdown(f"<div style='padding:10px; background-color:#DFF2BF; border-radius:10px;'><s>{t['task']}</s></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='padding:10px; background-color:#FFFACD; border-radius:10px;'>{t['task']}</div>", unsafe_allow_html=True)
        
        # Delete button
        with col3:
            if st.button("🗑️", key=f"delete_{i}"):
                st.session_state.tasks.pop(i)
                st.experimental_rerun()
else:
    st.info("No tasks yet. Add your first task above ⬆️")
