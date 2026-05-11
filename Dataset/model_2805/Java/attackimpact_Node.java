





import java.util.List;
import java.util.ArrayList;

public class attackimpact_Node  {

    private String tags;
    private String name;
    private String description;
    private String domains;



    public attackimpact_Node(
        String tags,        String name,        String description,        String domains    ) {
        this.tags = tags;
        this.name = name;
        this.description = description;
        this.domains = domains;
    }


    public String getTags() {
        return tags;
    }

    public void setTags(String tags) {
        this.tags = tags;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getDomains() {
        return domains;
    }

    public void setDomains(String domains) {
        this.domains = domains;
    }


}