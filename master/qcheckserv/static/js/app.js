const BACKGROUND_COLOR = "rgba(99, 255, 132, 0.2)";
const BORDER_COLOR = "rgb(99, 255, 132)";
const CROSSHAIR_COLOR = "rgb(99, 255, 132)";
const GRID_COLOR = "rgba(99, 255, 132, 0.1)";

const COLORS = [
    "99, 255, 132",
    "132, 99, 255",
    "255, 132, 99",
    "255, 99, 132",
    "39, 219, 242",
    "219, 242, 39",
];

function padNum(num, size) {
    num = num.toString();
    while (num.length < size) num = "0" + num;
    return num;
}

function formatDate(date) {
    let datePart = [
        date.getFullYear(),
        date.getMonth() + 1,
        date.getDate(),
    ].map((n, i) => n.toString().padStart(i === 4 ? 4 : 2, "0")).join("-");
    let timePart = [
        date.getHours(),
        date.getMinutes(),
        date.getSeconds()
    ].map((n, i) => n.toString().padStart(2, "0")).join(":");
    return datePart + " " + timePart;
  }

// Add alert line
function addLineToChart(chart, color, value) {
    if (!chart.config.options.plugins.annotation) {
        chart.config.options.plugins.annotation = { annotations: [] };
    }

    chart.config.options.plugins.annotation.annotations.push({
        type: 'line',
        mode: 'horizontal',
        scaleID: 'y',
        value: value,
        borderColor: color,
        borderWidth: 2,
    });

    chart.update();
}

function addData(chart, newData, datasetIndex = -1) {
    if (datasetIndex >= 0) {
        chart.data.datasets[datasetIndex].data.push(newData);
    } else {
        chart.data.datasets.forEach((dataset) => {
            dataset.data.push(newData);
        });
    }
    chart.update();
}

function addDataset(chart, dataset) {
    chart.config.data.datasets.push(dataset);
    chart.update();
}

function removeData(chart) {
    chart.data.labels.shift();
    chart.data.datasets.forEach((dataset) => {
        dataset.data.shift();
    });
    chart.update();
}

function createConfig(labelText, dataLabels, dataValues, yAxisUnit = '%') {
    return {
        type: "line",
        data: {
            labels: dataLabels,
            datasets: [
                {
                    label: labelText,
                    data: dataValues,
                    fill: true,
                    backgroundColor: BACKGROUND_COLOR,
                    borderColor: BORDER_COLOR,
                    lineTension: 0.01
                }
            ]
        },
        options: {
            hover: {
                intersect: false,
            },
            interaction: {
                intersect: false,
                mode: 'nearest',
                axis: 'x'
            },
            indexAxis: "x",
            responsive: false, // Use specified width and height
            scales: {
                y: {
                    ticks: {
                        callback: function(value, index, values) {
                            return value + ' ' + yAxisUnit;
                        }
                    },
                    grid: {
                        color: GRID_COLOR,
                    },
                    border: {
                        display: false,
                        dash: [5, 5],
                    },
                },
                x: {
                    grid: {
                        display: false,
                        lineWidth: 0,
                    },
                    type: 'time',
                    time: {
                        unit: "minute",
                        displayFormats: {
                            minute: 'yyyy-MM-dd HH:mm'
                        }
                    },
                    offsetAfterAutoskip: true,
                    ticks: {
                        source: 'labels',
                        minRotation: 45
                    }
                }
            },
            plugins: {
                tooltip: {
                    mode: "interpolate",
                    intersect: false,
                    animation: false,
                },
                crosshair: {
                    line: {
                        color: CROSSHAIR_COLOR,
                    },
                    snap: {
                        enabled: true
                    },
                    sync: {
                        enabled: true,
                        group: 1,
                        suppressTooltips: false,
                    },
                    zoom: {
                        enabled: false
                    }
                },
            },
        },
    };
}

function updateNavFocus(buttonIndex) {
    navLinks = document.querySelectorAll("nav a");
    navLinksMap = {}
    navLinks.forEach((a) => {
        a.classList.remove("active");
        navLinksMap[a.innerText.toLowerCase().split(' (')[0]] = a;
    });
    navLinksMap[buttonIndex].classList.add("active");
}

function updateFilterList() {
    filterListLinks = document.querySelectorAll("#filter-list a");
    timeframes = [3, 6, 12, 24, 72, 168];
    for(let i=0; i < timeframes.length; i++) {
        let hours = timeframes[i];
        let ms = new Date(Date.now() - hours * 60*60*1000);
        filterListLinks[i].setAttribute("hx-vals", '{"since": "' + formatDate(ms) + '"}');
    }
}

function translateUserRoleEnum(columnIndex) {
    tdListToTranslate = document.querySelectorAll(".item-groups .table-wrapper table td:nth-child(" + columnIndex + ")");
    tdListToTranslate.forEach((td) => {
        switch (td.innerText) {
            case '1':
                td.innerText = "ADMIN";
                break;
            default:
                td.innerText = "USER";
                break;
        }
    });
}

function getInputVal(id) {
    el = document.querySelector("#" + id);
    return el.value;
}

function hideOnClick(selector) {
    let elements = document.querySelectorAll(selector);
    elements.forEach((e) => {
        e.addEventListener('click', ()=> {
            e.classList.add("hidden");
        })
    });
}

function isDataLive() {
    let isDataLiveToggle = document.querySelector("#is-data-live-toggle");
    if (isDataLiveToggle.getAttribute("is-data-live") === "true") {
        return true;
    }
    return false;
}