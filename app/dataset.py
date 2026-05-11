TECHNICAL_DOCUMENTS = [
    """
    The distributed backend system handles peak load using horizontal scaling.
    Additional application instances are automatically deployed behind a load balancer
    whenever CPU usage exceeds predefined thresholds.
    """,

    """
    Caching is implemented using Redis to reduce database pressure.
    Frequently requested records are stored in memory which improves response times
    during high traffic conditions.
    """,

    """
    Fault tolerance is achieved through replication and automatic failover.
    If one node crashes, another node immediately takes over traffic handling.
    """,

    """
    The platform supports asynchronous event-driven processing using Kafka.
    This architecture enables high throughput and decouples services.
    """,

    """
    Authentication is implemented using OAuth2 and JWT tokens.
    Access tokens are validated through middleware before requests reach services.
    """,

    """
    Database performance is improved through indexing and query optimization.
    Slow queries are analyzed using monitoring dashboards.
    """,

    """
    The monitoring stack includes Prometheus and Grafana.
    Engineers receive alerts when latency or error rates exceed thresholds.
    """,

    """
    Container orchestration is handled using Kubernetes.
    Auto-scaling policies dynamically increase pod replicas based on traffic.
    """,

    """
    API gateway routing ensures secure communication between microservices.
    Rate limiting protects the platform against traffic spikes and abuse.
    """,

    """
    Disaster recovery procedures involve regular backups and multi-region deployments.
    System reliability is maintained even during regional outages.
    """
]