





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_IdentifiedElement  {

    private String name;
    private String label;



    public viewpoint_description_IdentifiedElement(
        String name,        String label    ) {
        this.name = name;
        this.label = label;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }


}