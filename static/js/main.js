// Tab switching
function showTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Remove active class from all buttons
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    
    // Show selected tab
    document.getElementById(tabName).classList.add('active');
    
    // Add active class to clicked button
    event.target.classList.add('active');
    
    // Load data for the tab if needed
    if (tabName === 'eda') loadEDAData();
    if (tabName === 'models') loadModelData();
    if (tabName === 'features') loadFeatureData();
}

// Format currency
function formatCurrency(value) {
    return '$' + value.toLocaleString();
}

// Format number
function formatNumber(value) {
    return value.toLocaleString();
}

// Load Overview Data
async function loadOverviewData() {
    try {
        const response = await fetch('/api/overview');
        const data = await response.json();
        
        document.getElementById('totalCustomers').textContent = formatNumber(data.totalCustomers);
        document.getElementById('churnRate').textContent = data.churnRate + '%';
        document.getElementById('revenueRisk').textContent = formatCurrency(data.totalRevenueRisk);
        document.getElementById('avgRevenue').textContent = formatCurrency(data.avgMonthlyRevenue);
        
        document.getElementById('bestModel').textContent = data.bestModel.name;
        document.getElementById('modelAccuracy').textContent = data.bestModel.accuracy + '%';
        document.getElementById('modelF1').textContent = data.bestModel.f1Score;
        
        document.getElementById('consCustomers').textContent = formatNumber(data.potentialImpact.conservative.customersSaved);
        document.getElementById('consRevenue').textContent = formatCurrency(data.potentialImpact.conservative.revenueProtected);
        document.getElementById('optCustomers').textContent = formatNumber(data.potentialImpact.optimistic.customersSaved);
        document.getElementById('optRevenue').textContent = formatCurrency(data.potentialImpact.optimistic.revenueProtected);
    } catch (error) {
        console.error('Error loading overview:', error);
    }
}

// Load EDA Data
let churnChart = null;
let contractChart = null;

async function loadEDAData() {
    try {
        // Churn Distribution
        const churnResponse = await fetch('/api/churn-distribution');
        const churnData = await churnResponse.json();
        
        if (churnChart) churnChart.destroy();
        const ctx1 = document.getElementById('churnChart').getContext('2d');
        churnChart = new Chart(ctx1, {
            type: 'pie',
            data: {
                labels: churnData.labels,
                datasets: [{
                    data: churnData.values,
                    backgroundColor: ['#2ecc71', '#e74c3c']
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'bottom'
                    }
                }
            }
        });
        
        // Contract Analysis
        const contractResponse = await fetch('/api/contract-analysis');
        const contractData = await contractResponse.json();
        
        if (contractChart) contractChart.destroy();
        const ctx2 = document.getElementById('contractChart').getContext('2d');
        contractChart = new Chart(ctx2, {
            type: 'bar',
            data: {
                labels: contractData.map(d => d.contract),
                datasets: [{
                    label: 'Churn Rate (%)',
                    data: contractData.map(d => d.churnRate),
                    backgroundColor: '#e74c3c'
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Churn Rate (%)'
                        }
                    }
                }
            }
        });
    } catch (error) {
        console.error('Error loading EDA data:', error);
    }
}

// Load Model Data
let modelChart = null;

async function loadModelData() {
    try {
        const response = await fetch('/api/model-performance');
        const data = await response.json();
        
        // Update chart
        if (modelChart) modelChart.destroy();
        const ctx = document.getElementById('modelChart').getContext('2d');
        modelChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.map(d => d.model),
                datasets: [{
                    label: 'Accuracy (%)',
                    data: data.map(d => d.accuracy),
                    backgroundColor: '#3498db'
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 100,
                        title: {
                            display: true,
                            text: 'Accuracy (%)'
                        }
                    }
                }
            }
        });
        
        // Update table
        const tbody = document.getElementById('modelTableBody');
        tbody.innerHTML = '';
        data.forEach(model => {
            const row = tbody.insertRow();
            row.innerHTML = `
                <td>${model.model}</td>
                <td>${model.accuracy}%</td>
                <td>${model.f1Score}</td>
            `;
        });
    } catch (error) {
        console.error('Error loading model data:', error);
    }
}

// Load Feature Data
let featureChart = null;

async function loadFeatureData() {
    try {
        const response = await fetch('/api/feature-importance');
        const data = await response.json();
        
        if (featureChart) featureChart.destroy();
        const ctx = document.getElementById('featureChart').getContext('2d');
        featureChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.features,
                datasets: [{
                    label: 'Importance',
                    data: data.importance,
                    backgroundColor: '#9b59b6'
                }]
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                plugins: {
                    legend: {
                        display: false
                    }
                },
                scales: {
                    x: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Importance'
                        }
                    }
                }
            }
        });
    } catch (error) {
        console.error('Error loading feature data:', error);
    }
}

// Test Random Customer
async function testRandomCustomer() {
    try {
        const response = await fetch('/api/predict-random');
        const data = await response.json();
        
        const resultsDiv = document.getElementById('testResults');
        resultsDiv.innerHTML = `
            <div class="prediction-card" style="grid-column: 1 / -1;">
                <h4>Customer #${data.customerId}</h4>
                <p><strong>Actual Churn:</strong> ${data.actualChurn}</p>
            </div>
        `;
        
        for (const [modelName, pred] of Object.entries(data.predictions)) {
            const riskClass = pred.riskLevel === 'HIGH' ? 'risk-high' : 
                            pred.riskLevel === 'MEDIUM' ? 'risk-medium' : 'risk-low';
            
            resultsDiv.innerHTML += `
                <div class="prediction-card">
                    <h4>${modelName.replace(/_/g, ' ').toUpperCase()}</h4>
                    <p><strong>Prediction:</strong> ${pred.prediction}</p>
                    <p><strong>Probability:</strong> ${pred.probability}%</p>
                    <p><strong>Risk Level:</strong> <span class="${riskClass}">${pred.riskLevel}</span></p>
                </div>
            `;
        }
    } catch (error) {
        console.error('Error testing customer:', error);
    }
}

// Load initial data when page loads
document.addEventListener('DOMContentLoaded', () => {
    loadOverviewData();
});
