
document.getElementById("submit-task").addEventListener("click", function() {
    var taskValue = document.getElementById("task-field").value;
    if(taskValue) {
        // Here you would normally send the task to the backend
        console.log("Task submitted:", taskValue);
        // Clear the input field after submission
        document.getElementById("task-field").value = '';
    } else {
        alert("Please enter a task.");
    }
});

