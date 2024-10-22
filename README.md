# Elasticsearch Cluster Setup Automation

This repository provides an automated way to set up an Elasticsearch cluster across multiple nodes using obfuscated setup scripts. The project includes encoded scripts for node configuration and multiple trigger scripts to execute them.

## Project Structure

```plaintext
elasticsearch_setup_auto/
├── LICENSE
├── README.md
├── src
│   ├── node1_setup.py
│   ├── node2_setup.py
│   └── node3_setup.py
└── trigger
    ├── node1_runner.sh
    ├── node2_runner.sh
    └── node3_runner.sh
```

## How to Use

Follow the steps below to set up your Elasticsearch cluster.

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/Ibrahimghali/elasticsearch-setup.git
```

Navigate to the project directory:

```bash
cd elasticsearch-setup
```

### 2. Know Your Node IP Addresses

Before running the setup scripts, ensure you know the IP addresses of the three nodes you will be configuring. This is crucial for the proper setup and communication between the nodes.

```bash
ip a
```

### 3. Run the Trigger Script

Navigate to the `trigger/` directory, which contains the encoded setup scripts:

```bash
cd trigger
```

Run the trigger script to decode and execute the node setup scripts. Choose the appropriate trigger script based on the node you want to set up:

```bash
bash node1_runner.sh  # For node-1
bash node2_runner.sh # For node-2
bash node3_runner.sh # For node-3
```

The selected script will automatically decode and set up the Elasticsearch cluster for the corresponding node based on the encoded files. Ensure the IP addresses of your nodes are properly configured during the process.

### 4. Verify the Cluster

Once the scripts have been executed, you can check the cluster status using the following command on any of the nodes:

```bash
curl -X GET "localhost:9200/_cluster/health?pretty"
```

This will give you details about the health and status of your Elasticsearch cluster.

## Additional Notes

- The original setup scripts are not included in the repository for security and simplicity reasons. They can be found in the `scripts/` directory.
- Make sure to review the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/index.html) for detailed configuration options and best practices.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
