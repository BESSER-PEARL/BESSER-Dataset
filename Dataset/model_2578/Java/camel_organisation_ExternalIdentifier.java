





import java.util.List;
import java.util.ArrayList;

public class camel_organisation_ExternalIdentifier  {

    private String identifier;
    private String description;



    public camel_organisation_ExternalIdentifier(
        String identifier,        String description    ) {
        this.identifier = identifier;
        this.description = description;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}