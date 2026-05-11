





import java.util.List;
import java.util.ArrayList;

public class uml_attributes  {

    private String group;





    private List<uml_attribute> uml_attributes;


    public uml_attributes(
        String group    ) {
        this.group = group;
        this.uml_attributes = new ArrayList<>();
    }

    public uml_attributes(
        String group        ArrayList<uml_attribute> uml_attributes    ) {
        this.group = group;
        this.uml_attributes = uml_attributes;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<uml_attribute> getUml_attributes() {
        return uml_attributes;
    }

    public void addUml_attribute(Uml_attribute uml_attribute) {
        this.uml_attributes.add(uml_attribute);
    }

}