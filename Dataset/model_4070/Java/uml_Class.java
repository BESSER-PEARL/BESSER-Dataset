





import java.util.List;
import java.util.ArrayList;

public class uml_Class extends Classifier {






    private List<uml_Class> uml_classs;




    private uml_Attribute uml_attribute;




    private uml_Association uml_association;




    private List<uml_Association> uml_associations;




    private List<uml_Association> uml_associations;




    private List<uml_Attribute> uml_attributes;




    private List<uml_Class> uml_classs;




    private uml_Association uml_association;


    public uml_Class(
    ) {
        super(
        );
        this.uml_classs = new ArrayList<>();
        this.uml_associations = new ArrayList<>();
        this.uml_associations = new ArrayList<>();
        this.uml_attributes = new ArrayList<>();
        this.uml_classs = new ArrayList<>();
    }

    public uml_Class(
        ArrayList<uml_Class> uml_classs,        ArrayList<uml_Association> uml_associations,        ArrayList<uml_Association> uml_associations,        ArrayList<uml_Attribute> uml_attributes,        ArrayList<uml_Class> uml_classs    ) {
        this.uml_classs = uml_classs;
        this.uml_associations = uml_associations;
        this.uml_associations = uml_associations;
        this.uml_attributes = uml_attributes;
        this.uml_classs = uml_classs;
    }


    public List<uml_Class> getUml_classs() {
        return uml_classs;
    }

    public void addUml_class(Uml_class uml_class) {
        this.uml_classs.add(uml_class);
    }
    public uml_Attribute getUml_attribute() {
        return uml_attribute;
    }

    public void setUml_attribute(uml_Attribute uml_attribute) {
        this.uml_attribute = uml_attribute;
    }
    public uml_Association getUml_association() {
        return uml_association;
    }

    public void setUml_association(uml_Association uml_association) {
        this.uml_association = uml_association;
    }
    public List<uml_Association> getUml_associations() {
        return uml_associations;
    }

    public void addUml_association(Uml_association uml_association) {
        this.uml_associations.add(uml_association);
    }
    public List<uml_Association> getUml_associations() {
        return uml_associations;
    }

    public void addUml_association(Uml_association uml_association) {
        this.uml_associations.add(uml_association);
    }
    public List<uml_Attribute> getUml_attributes() {
        return uml_attributes;
    }

    public void addUml_attribute(Uml_attribute uml_attribute) {
        this.uml_attributes.add(uml_attribute);
    }
    public List<uml_Class> getUml_classs() {
        return uml_classs;
    }

    public void addUml_class(Uml_class uml_class) {
        this.uml_classs.add(uml_class);
    }
    public uml_Association getUml_association() {
        return uml_association;
    }

    public void setUml_association(uml_Association uml_association) {
        this.uml_association = uml_association;
    }

}