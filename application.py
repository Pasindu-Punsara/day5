```python
from flask import Flask, render_template_string, jsonify
from datetime import datetime
import os

# Replace this with your actual GitHub repository URL
GITHUB_REPO_URL = "https://github.com/your-username/your-repo-name"

application = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>SLT-MOBITEL | AI & Data Unit</title>

    <script src="https://cdn.tailwindcss.com"></script>

    <script>
        function updateClock() {
            const now = new Date();

            document.getElementById('server-time').textContent =
                now.toISOString().replace('T', ' ').substring(0, 19) + ' UTC';
        }

        setInterval(updateClock, 1000);
        window.onload = updateClock;
    </script>

    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
        }

        .gradient-bg {
            background:
                radial-gradient(circle at top right,
                rgba(0, 120, 255, 0.18),
                transparent 40%),
                radial-gradient(circle at bottom left,
                rgba(220, 0, 50, 0.12),
                transparent 40%),
                #07111f;
        }

        .glass {
            background: rgba(10, 25, 45, 0.75);
            backdrop-filter: blur(10px);
        }
    </style>
</head>

<body class="gradient-bg text-white min-h-screen">

    <!-- Header -->
    <header class="border-b border-blue-900/50 glass">

        <div class="max-w-7xl mx-auto px-6 py-5
                    flex justify-between items-center">

            <div class="flex items-center space-x-4">

                <!-- SLT Logo Text -->
                <div class="flex items-center">

                    <div class="bg-blue-600 rounded-lg px-3 py-2
                                font-bold text-xl">
                        SLT
                    </div>

                    <div class="ml-3">
                        <div class="font-bold text-lg">
                            SLT-MOBITEL
                        </div>

                        <div class="text-xs text-blue-300">
                            AI & DATA UNIT
                        </div>
                    </div>

                </div>

            </div>

            <div class="hidden md:block">

                <span class="px-4 py-2 rounded-full
                             border border-green-500/40
                             bg-green-500/10
                             text-green-400 text-sm">

                    ● SYSTEM OPERATIONAL

                </span>

            </div>

        </div>

    </header>


    <!-- Main -->
    <main class="max-w-7xl mx-auto px-6 py-12">

        <!-- Hero -->
        <section class="text-center mb-12">

            <div class="inline-block mb-4
                        px-4 py-2 rounded-full
                        bg-blue-600/10
                        border border-blue-500/30
                        text-blue-300 text-sm">

                AI & DIGITAL TRANSFORMATION

            </div>

            <h1 class="text-4xl md:text-6xl font-bold mb-5">

                SLT-MOBITEL
                <span class="text-blue-400">
                    AI Platform
                </span>

            </h1>

            <p class="text-gray-400 max-w-2xl mx-auto text-lg">

                Empowering Sri Lanka's digital future through
                Artificial Intelligence, Data and Cloud Technologies.

            </p>

        </section>


        <!-- Status Cards -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-10">


            <!-- Application -->
            <div class="glass border border-blue-900/50
                        rounded-xl p-6">

                <div class="text-sm text-gray-400 mb-2">
                    APPLICATION STATUS
                </div>

                <div class="flex items-center space-x-3">

                    <div class="h-4 w-4 bg-green-500
                                rounded-full animate-pulse">
                    </div>

                    <span class="text-2xl font-bold text-green-400">
                        OPERATIONAL
                    </span>

                </div>

            </div>


            <!-- AWS -->
            <div class="glass border border-blue-900/50
                        rounded-xl p-6">

                <div class="text-sm text-gray-400 mb-2">
                    CLOUD PLATFORM
                </div>

                <div class="text-2xl font-bold text-blue-400">
                    AWS
                </div>

                <div class="text-sm text-gray-500 mt-1">
                    Elastic Beanstalk
                </div>

            </div>


            <!-- Region -->
            <div class="glass border border-blue-900/50
                        rounded-xl p-6">

                <div class="text-sm text-gray-400 mb-2">
                    AWS REGION
                </div>

                <div class="text-2xl font-bold">
                    {{ aws_region }}
                </div>

            </div>

        </div>


        <!-- Main Grid -->
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">


            <!-- Deployment -->
            <div class="lg:col-span-2 glass
                        border border-blue-900/50
                        rounded-xl p-8">

                <div class="flex justify-between
                            items-center mb-8">

                    <div>

                        <div class="text-sm text-blue-400 mb-2">
                            DEPLOYMENT
                        </div>

                        <h2 class="text-3xl font-bold">
                            SLT AI APPLICATION
                        </h2>

                    </div>

                    <div class="bg-green-500/10
                                border border-green-500/30
                                px-4 py-2 rounded-lg
                                text-green-400 font-bold">

                        SUCCESS

                    </div>

                </div>


                <div class="space-y-4 text-gray-300">

                    <div class="flex items-center">
                        <span class="text-green-400 mr-3">
                            ✓
                        </span>

                        AWS Elastic Beanstalk initialized
                    </div>

                    <div class="flex items-center">
                        <span class="text-green-400 mr-3">
                            ✓
                        </span>

                        Python / Flask application running
                    </div>

                    <div class="flex items-center">
                        <span class="text-green-400 mr-3">
                            ✓
                        </span>

                        Gunicorn application server active
                    </div>

                    <div class="flex items-center">
                        <span class="text-green-400 mr-3">
                            ✓
                        </span>

                        Application health check passed
                    </div>

                </div>


                <!-- Terminal -->
                <div class="mt-8 bg-black/60
                            border border-gray-800
                            rounded-lg p-5
                            font-mono text-sm">

                    <p class="text-gray-500">
                        $ slt-ai-system status
                    </p>

                    <p class="text-green-400 mt-2">
                        [OK] AI PLATFORM ONLINE
                    </p>

                    <p class="text-green-400">
                        [OK] CLOUD ENVIRONMENT ACTIVE
                    </p>

                    <p class="text-green-400">
                        [OK] APPLICATION HEALTHY
                    </p>

                    <p class="text-blue-400 mt-2">
                        [INFO] SLT-MOBITEL AI & DATA UNIT
                    </p>

                </div>

            </div>


            <!-- System Information -->
            <div class="glass border border-blue-900/50
                        rounded-xl p-6">

                <h2 class="text-xl font-bold mb-6">
                    SYSTEM INFORMATION
                </h2>


                <!-- Time -->
                <div class="bg-blue-950/40
                            border border-blue-900/50
                            rounded-lg p-4 mb-4">

                    <div class="text-xs text-gray-500">
                        SERVER TIME
                    </div>

                    <div id="server-time"
                         class="text-lg font-mono mt-1">

                        {{ current_time }}

                    </div>

                </div>


                <!-- Environment -->
                <div class="bg-blue-950/40
                            border border-blue-900/50
                            rounded-lg p-4 mb-4">

                    <div class="text-xs text-gray-500">
                        ENVIRONMENT
                    </div>

                    <div class="text-lg font-bold mt-1">
                        {{ env_name }}
                    </div>

                </div>


                <!-- Service -->
                <div class="bg-blue-950/40
                            border border-blue-900/50
                            rounded-lg p-4">

                    <div class="text-xs text-gray-500">
                        SERVICE
                    </div>

                    <div class="text-lg font-bold mt-1">
                        SLT AI PLATFORM
                    </div>

                </div>


                <!-- Buttons -->
                <div class="mt-6 space-y-3">

                    <a href="/health"
                       class="block text-center
                              bg-blue-600 hover:bg-blue-700
                              px-5 py-3 rounded-lg
                              font-bold transition">

                        CHECK SYSTEM HEALTH

                    </a>


                    <a href="{{ github_url }}"
                       target="_blank"
                       class="block text-center
                              border border-gray-700
                              hover:bg-gray-800
                              px-5 py-3 rounded-lg
                              transition">

                        VIEW SOURCE CODE

                    </a>

                </div>

            </div>

        </div>


        <!-- AI Services -->
        <section class="mt-10">

            <h2 class="text-2xl font-bold mb-6">
                AI & DATA SERVICES
            </h2>


            <div class="grid grid-cols-1 md:grid-cols-4 gap-4">

                <div class="glass border border-blue-900/50
                            rounded-lg p-5">

                    <div class="text-blue-400 text-2xl mb-2">
                        AI
                    </div>

                    <div class="font-bold">
                        Artificial Intelligence
                    </div>

                    <div class="text-sm text-gray-500 mt-1">
                        AI-powered enterprise solutions
                    </div>

                </div>


                <div class="glass border border-blue-900/50
                            rounded-lg p-5">

                    <div class="text-blue-400 text-2xl mb-2">
                        ML
                    </div>

                    <div class="font-bold">
                        Machine Learning
                    </div>

                    <div class="text-sm text-gray-500 mt-1">
                        Intelligent data-driven models
                    </div>

                </div>


                <div class="glass border border-blue-900/50
                            rounded-lg p-5">

                    <div class="text-blue-400 text-2xl mb-2">
                        ☁
                    </div>

                    <div class="font-bold">
                        Cloud Computing
                    </div>

                    <div class="text-sm text-gray-500 mt-1">
                        AWS cloud infrastructure
                    </div>

                </div>


                <div class="glass border border-blue-900/50
                            rounded-lg p-5">

                    <div class="text-blue-400 text-2xl mb-2">
                        DATA
                    </div>

                    <div class="font-bold">
                        Data Engineering
                    </div>

                    <div class="text-sm text-gray-500 mt-1">
                        Enterprise data solutions
                    </div>

                </div>

            </div>

        </section>

    </main>


    <!-- Footer -->
    <footer class="border-t border-blue-900/50
                   py-6 mt-10">

        <div class="max-w-7xl mx-auto px-6
                    text-center text-sm text-gray-500">

            © SLT-MOBITEL |
            AI & DATA UNIT |
            AWS Cloud Application

        </div>

    </footer>

</body>
</html>
"""


@application.route('/')
def home():

    now = datetime.utcnow().strftime(
        '%Y-%m-%d %H:%M:%S'
    )

    env_name = os.environ.get(
        'AWS_EB_ENVIRONMENT_NAME',
        'LOCAL_DEVELOPMENT'
    )

    aws_region = os.environ.get(
        'AWS_REGION',
        'us-east-1'
    )

    return render_template_string(
        HTML_TEMPLATE,
        current_time=now,
        github_url=GITHUB_REPO_URL,
        env_name=env_name,
        aws_region=aws_region
    )


@application.route('/health')
def health_check():

    return jsonify({

        "status": "operational",

        "service": "SLT AI Platform",

        "unit": "AI & Data Unit",

        "timestamp_utc":
            datetime.utcnow().isoformat()

    }), 200


if __name__ == '__main__':

    application.run(
        host='0.0.0.0',
        port=5000
    )
```
