





import java.util.List;
import java.util.ArrayList;

public class build_Category  {

    private String label;
    private String description;
    private String name;



    public build_Category(
        String label,        String description,        String name    ) {
        this.label = label;
        this.description = description;
        this.name = name;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
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