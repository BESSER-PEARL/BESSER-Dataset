





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_StructuredClassifier extends Classifier {






    private List<UML2WithID_Property> uml2withid_propertys;




    private List<UML2WithID_Property> uml2withid_propertys;




    private List<UML2WithID_ConnectableElement> uml2withid_connectableelements;


    public UML2WithID_StructuredClassifier(
    ) {
        super(
        );
        this.uml2withid_propertys = new ArrayList<>();
        this.uml2withid_propertys = new ArrayList<>();
        this.uml2withid_connectableelements = new ArrayList<>();
    }

    public UML2WithID_StructuredClassifier(
        ArrayList<UML2WithID_Property> uml2withid_propertys,        ArrayList<UML2WithID_Property> uml2withid_propertys,        ArrayList<UML2WithID_ConnectableElement> uml2withid_connectableelements    ) {
        this.uml2withid_propertys = uml2withid_propertys;
        this.uml2withid_propertys = uml2withid_propertys;
        this.uml2withid_connectableelements = uml2withid_connectableelements;
    }


    public List<UML2WithID_Property> getUml2withid_propertys() {
        return uml2withid_propertys;
    }

    public void addUml2withid_property(Uml2withid_property uml2withid_property) {
        this.uml2withid_propertys.add(uml2withid_property);
    }
    public List<UML2WithID_Property> getUml2withid_propertys() {
        return uml2withid_propertys;
    }

    public void addUml2withid_property(Uml2withid_property uml2withid_property) {
        this.uml2withid_propertys.add(uml2withid_property);
    }
    public List<UML2WithID_ConnectableElement> getUml2withid_connectableelements() {
        return uml2withid_connectableelements;
    }

    public void addUml2withid_connectableelement(Uml2withid_connectableelement uml2withid_connectableelement) {
        this.uml2withid_connectableelements.add(uml2withid_connectableelement);
    }

}