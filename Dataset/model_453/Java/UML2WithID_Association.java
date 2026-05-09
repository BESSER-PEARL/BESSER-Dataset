





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Association extends Classifier, Relationship {

    private boolean isDerived;





    private List<UML2WithID_Property> uml2withid_propertys;




    private List<UML2WithID_Type> uml2withid_types;




    private UML2WithID_Property uml2withid_property;




    private UML2WithID_Property uml2withid_property;




    private List<UML2WithID_Property> uml2withid_propertys;


    public UML2WithID_Association(
        boolean isDerived    ) {
        super(
        );
        this.isDerived = isDerived;
        this.uml2withid_propertys = new ArrayList<>();
        this.uml2withid_types = new ArrayList<>();
        this.uml2withid_propertys = new ArrayList<>();
    }

    public UML2WithID_Association(
        boolean isDerived        ArrayList<UML2WithID_Property> uml2withid_propertys,        ArrayList<UML2WithID_Type> uml2withid_types,        ArrayList<UML2WithID_Property> uml2withid_propertys    ) {
        this.isDerived = isDerived;
        this.uml2withid_propertys = uml2withid_propertys;
        this.uml2withid_types = uml2withid_types;
        this.uml2withid_propertys = uml2withid_propertys;
    }

    public boolean getIsderived() {
        return isDerived;
    }

    public void setIsderived(boolean isDerived) {
        this.isDerived = isDerived;
    }

    public List<UML2WithID_Property> getUml2withid_propertys() {
        return uml2withid_propertys;
    }

    public void addUml2withid_property(Uml2withid_property uml2withid_property) {
        this.uml2withid_propertys.add(uml2withid_property);
    }
    public List<UML2WithID_Type> getUml2withid_types() {
        return uml2withid_types;
    }

    public void addUml2withid_type(Uml2withid_type uml2withid_type) {
        this.uml2withid_types.add(uml2withid_type);
    }
    public UML2WithID_Property getUml2withid_property() {
        return uml2withid_property;
    }

    public void setUml2withid_property(UML2WithID_Property uml2withid_property) {
        this.uml2withid_property = uml2withid_property;
    }
    public UML2WithID_Property getUml2withid_property() {
        return uml2withid_property;
    }

    public void setUml2withid_property(UML2WithID_Property uml2withid_property) {
        this.uml2withid_property = uml2withid_property;
    }
    public List<UML2WithID_Property> getUml2withid_propertys() {
        return uml2withid_propertys;
    }

    public void addUml2withid_property(Uml2withid_property uml2withid_property) {
        this.uml2withid_propertys.add(uml2withid_property);
    }

}