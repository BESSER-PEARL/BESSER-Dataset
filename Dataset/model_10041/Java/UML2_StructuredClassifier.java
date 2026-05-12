





import java.util.List;
import java.util.ArrayList;

public class UML2_StructuredClassifier extends Classifier {






    private List<UML2_ConnectableElement> uml2_connectableelements;




    private List<UML2_Property> uml2_propertys;




    private List<UML2_Property> uml2_propertys;


    public UML2_StructuredClassifier(
    ) {
        super(
        );
        this.uml2_connectableelements = new ArrayList<>();
        this.uml2_propertys = new ArrayList<>();
        this.uml2_propertys = new ArrayList<>();
    }

    public UML2_StructuredClassifier(
        ArrayList<UML2_ConnectableElement> uml2_connectableelements,        ArrayList<UML2_Property> uml2_propertys,        ArrayList<UML2_Property> uml2_propertys    ) {
        this.uml2_connectableelements = uml2_connectableelements;
        this.uml2_propertys = uml2_propertys;
        this.uml2_propertys = uml2_propertys;
    }


    public List<UML2_ConnectableElement> getUml2_connectableelements() {
        return uml2_connectableelements;
    }

    public void addUml2_connectableelement(Uml2_connectableelement uml2_connectableelement) {
        this.uml2_connectableelements.add(uml2_connectableelement);
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