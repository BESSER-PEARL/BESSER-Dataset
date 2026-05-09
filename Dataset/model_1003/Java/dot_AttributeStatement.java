





import java.util.List;
import java.util.ArrayList;

public class dot_AttributeStatement extends Statement {

    private String type;





    private List<dot_Attribute> dot_attributes;


    public dot_AttributeStatement(
        String type    ) {
        super(
        );
        this.type = type;
        this.dot_attributes = new ArrayList<>();
    }

    public dot_AttributeStatement(
        String type        ArrayList<dot_Attribute> dot_attributes    ) {
        this.type = type;
        this.dot_attributes = dot_attributes;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<dot_Attribute> getDot_attributes() {
        return dot_attributes;
    }

    public void addDot_attribute(Dot_attribute dot_attribute) {
        this.dot_attributes.add(dot_attribute);
    }

}