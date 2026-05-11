





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedStructuredClassifier extends TracedClassifier {






    private List<uml_TracedProperty> uml_tracedpropertys;




    private List<uml_TracedProperty> uml_tracedpropertys;




    private List<uml_TracedConnector> uml_tracedconnectors;




    private List<uml_TracedConnectableElement> uml_tracedconnectableelements;


    public umlTrace_uml_TracedStructuredClassifier(
    ) {
        super(
        );
        this.uml_tracedpropertys = new ArrayList<>();
        this.uml_tracedpropertys = new ArrayList<>();
        this.uml_tracedconnectors = new ArrayList<>();
        this.uml_tracedconnectableelements = new ArrayList<>();
    }

    public umlTrace_uml_TracedStructuredClassifier(
        ArrayList<uml_TracedProperty> uml_tracedpropertys,        ArrayList<uml_TracedProperty> uml_tracedpropertys,        ArrayList<uml_TracedConnector> uml_tracedconnectors,        ArrayList<uml_TracedConnectableElement> uml_tracedconnectableelements    ) {
        this.uml_tracedpropertys = uml_tracedpropertys;
        this.uml_tracedpropertys = uml_tracedpropertys;
        this.uml_tracedconnectors = uml_tracedconnectors;
        this.uml_tracedconnectableelements = uml_tracedconnectableelements;
    }


    public List<uml_TracedProperty> getUml_tracedpropertys() {
        return uml_tracedpropertys;
    }

    public void addUml_tracedproperty(Uml_tracedproperty uml_tracedproperty) {
        this.uml_tracedpropertys.add(uml_tracedproperty);
    }
    public List<uml_TracedProperty> getUml_tracedpropertys() {
        return uml_tracedpropertys;
    }

    public void addUml_tracedproperty(Uml_tracedproperty uml_tracedproperty) {
        this.uml_tracedpropertys.add(uml_tracedproperty);
    }
    public List<uml_TracedConnector> getUml_tracedconnectors() {
        return uml_tracedconnectors;
    }

    public void addUml_tracedconnector(Uml_tracedconnector uml_tracedconnector) {
        this.uml_tracedconnectors.add(uml_tracedconnector);
    }
    public List<uml_TracedConnectableElement> getUml_tracedconnectableelements() {
        return uml_tracedconnectableelements;
    }

    public void addUml_tracedconnectableelement(Uml_tracedconnectableelement uml_tracedconnectableelement) {
        this.uml_tracedconnectableelements.add(uml_tracedconnectableelement);
    }

}