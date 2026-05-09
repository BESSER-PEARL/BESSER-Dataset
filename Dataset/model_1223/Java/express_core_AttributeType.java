





import java.util.List;
import java.util.ArrayList;

public class express_core_AttributeType  {






    private List<Attribute> attributes;


    public express_core_AttributeType(
    ) {
        this.attributes = new ArrayList<>();
    }

    public express_core_AttributeType(
        ArrayList<Attribute> attributes    ) {
        this.attributes = attributes;
    }


    public List<Attribute> getAttributes() {
        return attributes;
    }

    public void addAttribute(Attribute attribute) {
        this.attributes.add(attribute);
    }

}