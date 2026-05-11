





import java.util.List;
import java.util.ArrayList;

public class classLayout2Frontend_Entities_EntityModelElement  {

    private String name;
    private String description;
    private String displayName;



    public classLayout2Frontend_Entities_EntityModelElement(
        String name,        String description,        String displayName    ) {
        this.name = name;
        this.description = description;
        this.displayName = displayName;
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
    public String getDisplayname() {
        return displayName;
    }

    public void setDisplayname(String displayName) {
        this.displayName = displayName;
    }


}