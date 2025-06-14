using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Logging;
using NLog.Web;

var builder = WebApplication.CreateBuilder(args);

// Configure NLog for logging
builder.Logging.ClearProviders();
builder.Logging.SetMinimumLevel(LogLevel.Trace);
builder.Host.UseNLog();

// Add services (calls Startup.cs methods)
var startup = new SongsProject.Startup(builder.Configuration);
startup.ConfigureServices(builder.Services);

var app = builder.Build();

// Configure middleware pipeline (calls Startup.cs method)
startup.Configure(app, app.Environment);

app.Run();
