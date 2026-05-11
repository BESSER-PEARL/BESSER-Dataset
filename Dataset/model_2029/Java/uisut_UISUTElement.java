





import java.util.List;
import java.util.ArrayList;

public class uisut_UISUTElement  {

    private String name;
    private String id;
    private String description;



    public uisut_UISUTElement(
        String name,        String id,        String description    ) {
        this.name = name;
        this.id = id;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
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


}