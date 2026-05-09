





import java.util.List;
import java.util.ArrayList;

public class domain_ServerClaster extends InfrastructureComponent {






    private List<domain_Server> domain_servers;


    public domain_ServerClaster(
    ) {
        super(
        );
        this.domain_servers = new ArrayList<>();
    }

    public domain_ServerClaster(
        ArrayList<domain_Server> domain_servers    ) {
        this.domain_servers = domain_servers;
    }


    public List<domain_Server> getDomain_servers() {
        return domain_servers;
    }

    public void addDomain_server(Domain_server domain_server) {
        this.domain_servers.add(domain_server);
    }

}