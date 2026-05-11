





import java.util.List;
import java.util.ArrayList;

public class spinefm_ConfigurationModel_Configuration  {

    private String id;
    private String description;



    public spinefm_ConfigurationModel_Configuration(
        String id,        String description    ) {
        this.id = id;
        this.description = description;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}