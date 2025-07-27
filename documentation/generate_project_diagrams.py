import graphviz
import os
import sys
import shutil
from typing import Optional

def check_dependencies() -> tuple[bool, str]:
    """Check if all required dependencies are installed."""
    # Check if graphviz is installed
    if shutil.which('dot') is None:
        install_instructions = """
Error: Graphviz is not installed. Please install it using:

For macOS:
    brew install graphviz

For Ubuntu/Debian:
    sudo apt-get install graphviz

For Windows:
    1. Download from https://graphviz.org/download/
    2. Add to system PATH

After installation, restart your terminal and try again.
"""
        return False, install_instructions
    return True, "All dependencies found"

OUTPUT_DIR = '../documentation/diagrams'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def safe_render(dot: graphviz.Digraph, filename: str) -> Optional[str]:
    """Safely render a diagram with error handling."""
    try:
        return dot.render(f'{OUTPUT_DIR}/{filename}', view=False)
    except graphviz.backend.execute.ExecutableNotFound:
        print(f"Error: Failed to generate {filename}.png - Graphviz not found")
        return None
    except Exception as e:
        print(f"Error generating {filename}.png: {str(e)}")
        return None

def create_dfd_level0():
    dot = graphviz.Digraph('DFD_Level0', format='png')
    dot.attr(bgcolor='white')
    
    # Add nodes and edges for DFD Level 0
    dot.node('User', 'User')
    dot.node('System', 'Quantum K-means\nClustering System')
    dot.node('Database', 'Data\nStorage')
    
    dot.edge('User', 'System', 'Input Data')
    dot.edge('System', 'User', 'Clustering Results')
    dot.edge('System', 'Database', 'Store Results')
    dot.edge('Database', 'System', 'Retrieve Data')
    
    safe_render(dot, 'dfd_level0')

def create_dfd_level1():
    dot = graphviz.Digraph('DFD_Level1', format='png')
    dot.attr(bgcolor='white')
    
    # Add nodes for major components
    dot.node('Input', 'Data Input')
    dot.node('Preprocess', 'Data\nPreprocessing')
    dot.node('Quantum', 'Quantum\nProcessing')
    dot.node('Classical', 'Classical\nProcessing')
    dot.node('Result', 'Result\nVisualization')
    
    # Add edges showing data flow
    dot.edge('Input', 'Preprocess')
    dot.edge('Preprocess', 'Quantum')
    dot.edge('Preprocess', 'Classical')
    dot.edge('Quantum', 'Result')
    dot.edge('Classical', 'Result')
    
    safe_render(dot, 'dfd_level1')

def create_activity_diagram():
    dot = graphviz.Digraph('Activity', format='png')
    dot.attr(bgcolor='white')
    
    # Activity diagram nodes and edges
    activities = [
        'Start',
        'Load Data',
        'Preprocess',
        'Initialize Quantum Circuit',
        'Calculate Distances',
        'Update Centroids',
        'Check Convergence',
        'Generate Results',
        'End'
    ]
    
    for i, activity in enumerate(activities):
        dot.node(f'A{i}', activity)
        if i > 0:
            dot.edge(f'A{i-1}', f'A{i}')
    
    safe_render(dot, 'activity_diagram')

def create_flowchart():
    dot = graphviz.Digraph('Flowchart', format='png')
    dot.attr(bgcolor='white')
    
    # Flowchart nodes and logic
    dot.node('start', 'Start', shape='oval')
    dot.node('input', 'Input Data')
    dot.node('init', 'Initialize\nQuantum Circuit')
    dot.node('process', 'Process Data')
    dot.node('check', 'Converged?', shape='diamond')
    dot.node('output', 'Output Results')
    dot.node('end', 'End', shape='oval')
    
    dot.edge('start', 'input')
    dot.edge('input', 'init')
    dot.edge('init', 'process')
    dot.edge('process', 'check')
    dot.edge('check', 'process', 'No')
    dot.edge('check', 'output', 'Yes')
    dot.edge('output', 'end')
    
    safe_render(dot, 'flowchart')

def create_class_diagram():
    dot = graphviz.Digraph('Class_Diagram', format='png')
    dot.attr(bgcolor='white')
    
    # Class definitions
    classes = {
        'QuantumKMeans': [
            'n_clusters: int',
            'quantum_circuit: QuantumCircuit',
            'backend: QiskitBackend',
            'fit()',
            'predict()',
            '_create_circuit()'
        ],
        'DataPreprocessor': [
            'scaler: StandardScaler',
            'normalize()',
            'transform()',
            'inverse_transform()'
        ],
        'Visualizer': [
            'plot_results()',
            'plot_clusters()',
            'save_figures()'
        ]
    }
    
    for class_name, members in classes.items():
        label = f'{class_name}|' + '\\l'.join(members) + '\\l'
        dot.node(class_name, label, shape='record')
    
    # Add relationships
    dot.edge('QuantumKMeans', 'DataPreprocessor')
    dot.edge('QuantumKMeans', 'Visualizer')
    
    safe_render(dot, 'class_diagram')

def create_er_diagram():
    dot = graphviz.Digraph('ER_Diagram', format='png')
    dot.attr(bgcolor='white')
    
    # Entity definitions
    entities = {
        'Dataset': ['id', 'name', 'features'],
        'Cluster': ['id', 'centroid', 'size'],
        'Result': ['id', 'accuracy', 'time']
    }
    
    for entity, attributes in entities.items():
        label = f'{entity}|' + '\\l'.join(attributes) + '\\l'
        dot.node(entity, label, shape='record')
    
    # Add relationships
    dot.edge('Dataset', 'Cluster', 'belongs to')
    dot.edge('Cluster', 'Result', 'produces')
    
    safe_render(dot, 'er_diagram')

def create_sequence_diagram():
    dot = graphviz.Digraph('Sequence_Diagram', format='png')
    dot.attr(bgcolor='white')
    
    # Lifeline objects
    objects = ['User', 'Interface', 'QuantumKMeans', 'Circuit', 'Visualizer']
    for obj in objects:
        dot.node(obj, obj)
    
    # Messages
    messages = [
        ('User', 'Interface', 'load_data()'),
        ('Interface', 'QuantumKMeans', 'initialize()'),
        ('QuantumKMeans', 'Circuit', 'create_circuit()'),
        ('Circuit', 'QuantumKMeans', 'return circuit'),
        ('QuantumKMeans', 'Visualizer', 'plot_results()'),
        ('Visualizer', 'User', 'show_visualization()')
    ]
    
    for i, (src, dst, label) in enumerate(messages):
        dot.edge(src, dst, f'{i+1}: {label}')
    
    safe_render(dot, 'sequence_diagram')

if __name__ == "__main__":
    # Check dependencies first
    deps_ok, message = check_dependencies()
    if not deps_ok:
        print(message)
        sys.exit(1)
    
    # Create diagrams with error handling
    diagrams = [
        ('DFD Level 0', create_dfd_level0),
        ('DFD Level 1', create_dfd_level1),
        ('Activity Diagram', create_activity_diagram),
        ('Flowchart', create_flowchart),
        ('Class Diagram', create_class_diagram),
        ('ER Diagram', create_er_diagram),
        ('Sequence Diagram', create_sequence_diagram)
    ]
    
    success_count = 0
    for name, func in diagrams:
        try:
            func()
            success_count += 1
            print(f"✓ Generated {name}")
        except Exception as e:
            print(f"✗ Failed to generate {name}: {str(e)}")
    
    print(f"\nCompleted: {success_count}/{len(diagrams)} diagrams generated successfully")
    print(f"Output directory: {os.path.abspath(OUTPUT_DIR)}")
