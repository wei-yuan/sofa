#!/usr/bin/env python3
class Filter:
    keyword = None
    color = None

    def __init__(self, keyword, color):
        self.keyword = keyword
        self.color = color


class SOFA_Config:
    cpu_filters = []
    gpu_filters = []
    net_filters = []
    perf_events = 'cycles,instructions' 
    verbose = False
    num_iterations = 20
    num_swarms = 20
    cpu_top_k = 20
    plot_ratio = 1
    viz_port = 8000
    cpu_time_offset = 0
    profile_all_cpus = False
    enable_aisi = False
    enable_hsg = False
    enable_vmstat = False
    enable_pcm = False
    cuda_api_tracing = False
    script_path = ''
