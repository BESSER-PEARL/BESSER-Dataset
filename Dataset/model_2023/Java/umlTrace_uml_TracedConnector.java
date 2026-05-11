





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedConnector extends TracedFeature {






    private uml_TracedAssociation uml_tracedassociation;




    private List<uml_TracedConnectorEnd> uml_tracedconnectorends;




    private List<uml_TracedConnector> uml_tracedconnectors;


    public umlTrace_uml_TracedConnector(
    ) {
        super(
        );
        this.uml_tracedconnectorends = new ArrayList<>();
        this.uml_tracedconnectors = new ArrayList<>();
    }

    public umlTrace_uml_TracedConnector(
        ArrayList<uml_TracedConnectorEnd> uml_tracedconnectorends,        ArrayList<uml_TracedConnector> uml_tracedconnectors    ) {
        this.uml_tracedconnectorends = uml_tracedconnectorends;
        this.uml_tracedconnectors = uml_tracedconnectors;
    }


    public uml_TracedAssociation getUml_tracedassociation() {
        return uml_tracedassociation;
    }

    public void setUml_tracedassociation(uml_TracedAssociation uml_tracedassociation) {
        this.uml_tracedassociation = uml_tracedassociation;
    }
    public List<uml_TracedConnectorEnd> getUml_tracedconnectorends() {
        return uml_tracedconnectorends;
    }

    public void addUml_tracedconnectorend(Uml_tracedconnectorend uml_tracedconnectorend) {
        this.uml_tracedconnectorends.add(uml_tracedconnectorend);
    }
    public List<uml_TracedConnector> getUml_tracedconnectors() {
        return uml_tracedconnectors;
    }

    public void addUml_tracedconnector(Uml_tracedconnector uml_tracedconnector) {
        this.uml_tracedconnectors.add(uml_tracedconnector);
    }

}