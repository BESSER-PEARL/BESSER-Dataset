





import java.util.List;
import java.util.ArrayList;

public class spinefm_ConfigurationModel_CompositeConfiguration  {

    private String description;
    private String name;





    private List<Link> links;


    public spinefm_ConfigurationModel_CompositeConfiguration(
        String description,        String name    ) {
        this.description = description;
        this.name = name;
        this.links = new ArrayList<>();
    }

    public spinefm_ConfigurationModel_CompositeConfiguration(
        String description,        String name        ArrayList<Link> links    ) {
        this.description = description;
        this.name = name;
        this.links = links;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Link> getLinks() {
        return links;
    }

    public void addLink(Link link) {
        this.links.add(link);
    }

}