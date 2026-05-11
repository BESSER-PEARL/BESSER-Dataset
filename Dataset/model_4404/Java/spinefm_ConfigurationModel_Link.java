





import java.util.List;
import java.util.ArrayList;

public class spinefm_ConfigurationModel_Link  {

    private String id;





    private Configuration configuration;




    private DEAssociation deassociation;




    private Configuration configuration;


    public spinefm_ConfigurationModel_Link(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Configuration getConfiguration() {
        return configuration;
    }

    public void setConfiguration(Configuration configuration) {
        this.configuration = configuration;
    }
    public DEAssociation getDeassociation() {
        return deassociation;
    }

    public void setDeassociation(DEAssociation deassociation) {
        this.deassociation = deassociation;
    }
    public Configuration getConfiguration() {
        return configuration;
    }

    public void setConfiguration(Configuration configuration) {
        this.configuration = configuration;
    }

}