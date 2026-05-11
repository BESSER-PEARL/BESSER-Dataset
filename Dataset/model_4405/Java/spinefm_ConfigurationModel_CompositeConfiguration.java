





import java.util.List;
import java.util.ArrayList;

public class spinefm_ConfigurationModel_CompositeConfiguration  {

    private String name;





    private List<Configuration> configurations;




    private List<Link> links;


    public spinefm_ConfigurationModel_CompositeConfiguration(
        String name    ) {
        this.name = name;
        this.configurations = new ArrayList<>();
        this.links = new ArrayList<>();
    }

    public spinefm_ConfigurationModel_CompositeConfiguration(
        String name        ArrayList<Configuration> configurations,        ArrayList<Link> links    ) {
        this.name = name;
        this.configurations = configurations;
        this.links = links;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Configuration> getConfigurations() {
        return configurations;
    }

    public void addConfiguration(Configuration configuration) {
        this.configurations.add(configuration);
    }
    public List<Link> getLinks() {
        return links;
    }

    public void addLink(Link link) {
        this.links.add(link);
    }

}