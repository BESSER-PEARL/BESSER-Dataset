





import java.util.List;
import java.util.ArrayList;

public class spinefm_ConfigurationModel_Configuration  {

    private String description;
    private String id;





    private DomainElement domainelement;


    public spinefm_ConfigurationModel_Configuration(
        String description,        String id    ) {
        this.description = description;
        this.id = id;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public DomainElement getDomainelement() {
        return domainelement;
    }

    public void setDomainelement(DomainElement domainelement) {
        this.domainelement = domainelement;
    }

}