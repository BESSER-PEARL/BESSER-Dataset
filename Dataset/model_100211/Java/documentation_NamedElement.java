





import java.util.List;
import java.util.ArrayList;

public class documentation_NamedElement  {

    private String label;
    private String id;
    private String name;



    public documentation_NamedElement(
        String label,        String id,        String name    ) {
        this.label = label;
        this.id = id;
        this.name = name;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}