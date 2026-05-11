





import java.util.List;
import java.util.ArrayList;

public class uml_Class extends Classifier {






    private uml_Attribute uml_attribute;




    private List<uml_Class> uml_classs;




    private uml_Class uml_class;




    private List<uml_Attribute> uml_attributes;


    public uml_Class(
    ) {
        super(
        );
        this.uml_classs = new ArrayList<>();
        this.uml_attributes = new ArrayList<>();
    }

    public uml_Class(
        ArrayList<uml_Class> uml_classs,        ArrayList<uml_Attribute> uml_attributes    ) {
        this.uml_classs = uml_classs;
        this.uml_attributes = uml_attributes;
    }


    public uml_Attribute getUml_attribute() {
        return uml_attribute;
    }

    public void setUml_attribute(uml_Attribute uml_attribute) {
        this.uml_attribute = uml_attribute;
    }
    public List<uml_Class> getUml_classs() {
        return uml_classs;
    }

    public void addUml_class(Uml_class uml_class) {
        this.uml_classs.add(uml_class);
    }
    public uml_Class getUml_class() {
        return uml_class;
    }

    public void setUml_class(uml_Class uml_class) {
        this.uml_class = uml_class;
    }
    public List<uml_Attribute> getUml_attributes() {
        return uml_attributes;
    }

    public void addUml_attribute(Uml_attribute uml_attribute) {
        this.uml_attributes.add(uml_attribute);
    }

}