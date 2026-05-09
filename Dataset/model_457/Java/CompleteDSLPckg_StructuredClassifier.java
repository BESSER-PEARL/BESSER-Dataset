





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_StructuredClassifier extends Classifier {






    private List<CompleteDSLPckg_Property> completedslpckg_propertys;




    private List<CompleteDSLPckg_Property> completedslpckg_propertys;




    private List<CompleteDSLPckg_ConnectableElement> completedslpckg_connectableelements;




    private List<CompleteDSLPckg_Connector> completedslpckg_connectors;


    public CompleteDSLPckg_StructuredClassifier(
    ) {
        super(
        );
        this.completedslpckg_propertys = new ArrayList<>();
        this.completedslpckg_propertys = new ArrayList<>();
        this.completedslpckg_connectableelements = new ArrayList<>();
        this.completedslpckg_connectors = new ArrayList<>();
    }

    public CompleteDSLPckg_StructuredClassifier(
        ArrayList<CompleteDSLPckg_Property> completedslpckg_propertys,        ArrayList<CompleteDSLPckg_Property> completedslpckg_propertys,        ArrayList<CompleteDSLPckg_ConnectableElement> completedslpckg_connectableelements,        ArrayList<CompleteDSLPckg_Connector> completedslpckg_connectors    ) {
        this.completedslpckg_propertys = completedslpckg_propertys;
        this.completedslpckg_propertys = completedslpckg_propertys;
        this.completedslpckg_connectableelements = completedslpckg_connectableelements;
        this.completedslpckg_connectors = completedslpckg_connectors;
    }


    public List<CompleteDSLPckg_Property> getCompletedslpckg_propertys() {
        return completedslpckg_propertys;
    }

    public void addCompletedslpckg_property(Completedslpckg_property completedslpckg_property) {
        this.completedslpckg_propertys.add(completedslpckg_property);
    }
    public List<CompleteDSLPckg_Property> getCompletedslpckg_propertys() {
        return completedslpckg_propertys;
    }

    public void addCompletedslpckg_property(Completedslpckg_property completedslpckg_property) {
        this.completedslpckg_propertys.add(completedslpckg_property);
    }
    public List<CompleteDSLPckg_ConnectableElement> getCompletedslpckg_connectableelements() {
        return completedslpckg_connectableelements;
    }

    public void addCompletedslpckg_connectableelement(Completedslpckg_connectableelement completedslpckg_connectableelement) {
        this.completedslpckg_connectableelements.add(completedslpckg_connectableelement);
    }
    public List<CompleteDSLPckg_Connector> getCompletedslpckg_connectors() {
        return completedslpckg_connectors;
    }

    public void addCompletedslpckg_connector(Completedslpckg_connector completedslpckg_connector) {
        this.completedslpckg_connectors.add(completedslpckg_connector);
    }

}