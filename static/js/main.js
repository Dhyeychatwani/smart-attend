// SmartAttend — main.js
// Auto-refresh the dashboard every 30 seconds when attendance is being marked
setInterval(() => {
  const url = new URL(window.location.href);
  if (!url.searchParams.get('date')) {
    // Only auto-refresh on "All Dates" view to show live updates
    window.location.reload();
  }
}, 30000);
