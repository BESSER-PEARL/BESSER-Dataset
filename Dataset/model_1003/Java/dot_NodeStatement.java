





import java.util.List;
import java.util.ArrayList;

public class dot_NodeStatement extends Statement {






    private List<dot_Attribute> dot_attributes;


    public dot_NodeStatement(
    ) {
        super(
        );
        this.dot_attributes = new ArrayList<>();
    }

    public dot_NodeStatement(
        ArrayList<dot_Attribute> dot_attributes    ) {
        this.dot_attributes = dot_attributes;
    }


    public List<dot_Attribute> getDot_attributes() {
        return dot_attributes;
    }

    public void addDot_attribute(Dot_attribute dot_attribute) {
        this.dot_attributes.add(dot_attribute);
    }

}