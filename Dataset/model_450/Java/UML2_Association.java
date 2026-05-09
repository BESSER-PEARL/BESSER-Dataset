





import java.util.List;
import java.util.ArrayList;

public class UML2_Association extends Classifier, Relationship {

    private boolean isDerived;





    private List<UML2_Type> uml2_types;




    private List<UML2_Property> uml2_propertys;




    private UML2_Property uml2_property;




    private UML2_Property uml2_property;




    private List<UML2_Property> uml2_propertys;


    public UML2_Association(
        boolean isDerived    ) {
        super(
        );
        this.isDerived = isDerived;
        this.uml2_types = new ArrayList<>();
        this.uml2_propertys = new ArrayList<>();
        this.uml2_propertys = new ArrayList<>();
    }

    public UML2_Association(
        boolean isDerived        ArrayList<UML2_Type> uml2_types,        ArrayList<UML2_Property> uml2_propertys,        ArrayList<UML2_Property> uml2_propertys    ) {
        this.isDerived = isDerived;
        this.uml2_types = uml2_types;
        this.uml2_propertys = uml2_propertys;
        this.uml2_propertys = uml2_propertys;
    }

    public boolean getIsderived() {
        return isDerived;
    }

    public void setIsderived(boolean isDerived) {
        this.isDerived = isDerived;
    }

    public List<UML2_Type> getUml2_types() {
        return uml2_types;
    }

    public void addUml2_type(Uml2_type uml2_type) {
        this.uml2_types.add(uml2_type);
    }
    public List<UML2_Property> getUml2_propertys() {
        return uml2_propertys;
    }

    public void addUml2_property(Uml2_property uml2_property) {
        this.uml2_propertys.add(uml2_property);
    }
    public UML2_Property getUml2_property() {
        return uml2_property;
    }

    public void setUml2_property(UML2_Property uml2_property) {
        this.uml2_property = uml2_property;
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

}