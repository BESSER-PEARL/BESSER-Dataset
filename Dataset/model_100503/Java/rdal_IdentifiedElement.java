





import java.util.List;
import java.util.ArrayList;

public class rdal_IdentifiedElement  {

    private String id;
    private String description;
    private String name;



    public rdal_IdentifiedElement(
        String id,        String description,        String name    ) {
        this.id = id;
        this.description = description;
        this.name = name;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}