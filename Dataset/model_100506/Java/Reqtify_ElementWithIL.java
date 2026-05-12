





import java.util.List;
import java.util.ArrayList;

public class Reqtify_ElementWithIL extends TypedElement {

    private String name;
    private String label;



    public Reqtify_ElementWithIL(
        String name,        String label    ) {
        super(
        );
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