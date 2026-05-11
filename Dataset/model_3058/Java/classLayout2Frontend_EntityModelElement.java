





import java.util.List;
import java.util.ArrayList;

public class classLayout2Frontend_EntityModelElement  {

    private String displayName;
    private String description;
    private String name;



    public classLayout2Frontend_EntityModelElement(
        String displayName,        String description,        String name    ) {
        this.displayName = displayName;
        this.description = description;
        this.name = name;
    }


    public String getDisplayname() {
        return displayName;
    }

    public void setDisplayname(String displayName) {
        this.displayName = displayName;
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