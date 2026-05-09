





import java.util.List;
import java.util.ArrayList;

public class UML2_Association extends Relationship, Classifier {






    private UML2_Property uml2_property;




    private List<UML2_Property> uml2_propertys;




    private List<UML2_Property> uml2_propertys;


    public UML2_Association(
    ) {
        super(
        );
        this.uml2_propertys = new ArrayList<>();
        this.uml2_propertys = new ArrayList<>();
    }

    public UML2_Association(
        ArrayList<UML2_Property> uml2_propertys,        ArrayList<UML2_Property> uml2_propertys    ) {
        this.uml2_propertys = uml2_propertys;
        this.uml2_propertys = uml2_propertys;
    }


    public UML2_Property getUml2_property() {
        return uml2_property;
    }

    public void setUml2_property(UML2_Property uml2_property) {
        this.uml2_property = uml2_property;
    }
    public List<UML2_Property> getUml2_propertys() {
        return uml2_propertys;
    }

    public void addUml2_property(Uml2_property uml2_property) {
        this.uml2_propertys.add(uml2_property);
    }
    public List<UML2_Property> getUml2_propertys() {
        return uml2_propertys;
    }

    public void addUml2_property(Uml2_property uml2_property) {
        this.uml2_propertys.add(uml2_property);
    }

}