





import java.util.List;
import java.util.ArrayList;

public class uml_Classifier extends PackageElement {






    private uml_Attribute uml_attribute;




    private List<uml_Attribute> uml_attributes;


    public uml_Classifier(
    ) {
        super(
        );
        this.uml_attributes = new ArrayList<>();
    }

    public uml_Classifier(
        ArrayList<uml_Attribute> uml_attributes    ) {
        this.uml_attributes = uml_attributes;
    }


    public uml_Attribute getUml_attribute() {
        return uml_attribute;
    }

    public void setUml_attribute(uml_Attribute uml_attribute) {
        this.uml_attribute = uml_attribute;
    }
    public List<uml_Attribute> getUml_attributes() {
        return uml_attributes;
    }

    public void addUml_attribute(Uml_attribute uml_attribute) {
        this.uml_attributes.add(uml_attribute);
    }

}