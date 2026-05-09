





import java.util.List;
import java.util.ArrayList;

public class c_sharp_attributes_Attributes  {






    private List<Attribute> attributes;




    private AttributeTarget attributetarget;


    public c_sharp_attributes_Attributes(
    ) {
        this.attributes = new ArrayList<>();
    }

    public c_sharp_attributes_Attributes(
        ArrayList<Attribute> attributes    ) {
        this.attributes = attributes;
    }


    public List<Attribute> getAttributes() {
        return attributes;
    }

    public void addAttribute(Attribute attribute) {
        this.attributes.add(attribute);
    }
    public AttributeTarget getAttributetarget() {
        return attributetarget;
    }

    public void setAttributetarget(AttributeTarget attributetarget) {
        this.attributetarget = attributetarget;
    }

}