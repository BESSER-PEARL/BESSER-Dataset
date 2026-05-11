





import java.util.List;
import java.util.ArrayList;

public class umlMM_Class extends Classifier {






    private umlMM_Associaton umlmm_associaton;




    private List<umlMM_Associaton> umlmm_associatons;




    private List<umlMM_Attribute> umlmm_attributes;




    private List<umlMM_Associaton> umlmm_associatons;




    private umlMM_Associaton umlmm_associaton;




    private umlMM_Attribute umlmm_attribute;


    public umlMM_Class(
    ) {
        super(
        );
        this.umlmm_associatons = new ArrayList<>();
        this.umlmm_attributes = new ArrayList<>();
        this.umlmm_associatons = new ArrayList<>();
    }

    public umlMM_Class(
        ArrayList<umlMM_Associaton> umlmm_associatons,        ArrayList<umlMM_Attribute> umlmm_attributes,        ArrayList<umlMM_Associaton> umlmm_associatons    ) {
        this.umlmm_associatons = umlmm_associatons;
        this.umlmm_attributes = umlmm_attributes;
        this.umlmm_associatons = umlmm_associatons;
    }


    public umlMM_Associaton getUmlmm_associaton() {
        return umlmm_associaton;
    }

    public void setUmlmm_associaton(umlMM_Associaton umlmm_associaton) {
        this.umlmm_associaton = umlmm_associaton;
    }
    public List<umlMM_Associaton> getUmlmm_associatons() {
        return umlmm_associatons;
    }

    public void addUmlmm_associaton(Umlmm_associaton umlmm_associaton) {
        this.umlmm_associatons.add(umlmm_associaton);
    }
    public List<umlMM_Attribute> getUmlmm_attributes() {
        return umlmm_attributes;
    }

    public void addUmlmm_attribute(Umlmm_attribute umlmm_attribute) {
        this.umlmm_attributes.add(umlmm_attribute);
    }
    public List<umlMM_Associaton> getUmlmm_associatons() {
        return umlmm_associatons;
    }

    public void addUmlmm_associaton(Umlmm_associaton umlmm_associaton) {
        this.umlmm_associatons.add(umlmm_associaton);
    }
    public umlMM_Associaton getUmlmm_associaton() {
        return umlmm_associaton;
    }

    public void setUmlmm_associaton(umlMM_Associaton umlmm_associaton) {
        this.umlmm_associaton = umlmm_associaton;
    }
    public umlMM_Attribute getUmlmm_attribute() {
        return umlmm_attribute;
    }

    public void setUmlmm_attribute(umlMM_Attribute umlmm_attribute) {
        this.umlmm_attribute = umlmm_attribute;
    }

}