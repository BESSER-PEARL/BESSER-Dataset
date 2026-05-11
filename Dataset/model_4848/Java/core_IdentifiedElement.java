





import java.util.List;
import java.util.ArrayList;

public class core_IdentifiedElement  {

    private String name;
    private String description;
    private String id;



    public core_IdentifiedElement(
        String name,        String description,        String id    ) {
        this.name = name;
        this.description = description;
        this.id = id;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}