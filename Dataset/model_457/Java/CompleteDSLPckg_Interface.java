





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Interface extends Classifier {






    private List<CompleteDSLPckg_Property> completedslpckg_propertys;




    private CompleteDSLPckg_Component completedslpckg_component;




    private CompleteDSLPckg_Property completedslpckg_property;




    private CompleteDSLPckg_Component completedslpckg_component;




    private List<CompleteDSLPckg_Interface> completedslpckg_interfaces;




    private CompleteDSLPckg_Classifier completedslpckg_classifier;


    public CompleteDSLPckg_Interface(
    ) {
        super(
        );
        this.completedslpckg_propertys = new ArrayList<>();
        this.completedslpckg_interfaces = new ArrayList<>();
    }

    public CompleteDSLPckg_Interface(
        ArrayList<CompleteDSLPckg_Property> completedslpckg_propertys,        ArrayList<CompleteDSLPckg_Interface> completedslpckg_interfaces    ) {
        this.completedslpckg_propertys = completedslpckg_propertys;
        this.completedslpckg_interfaces = completedslpckg_interfaces;
    }


    public List<CompleteDSLPckg_Property> getCompletedslpckg_propertys() {
        return completedslpckg_propertys;
    }

    public void addCompletedslpckg_property(Completedslpckg_property completedslpckg_property) {
        this.completedslpckg_propertys.add(completedslpckg_property);
    }
    public CompleteDSLPckg_Component getCompletedslpckg_component() {
        return completedslpckg_component;
    }

    public void setCompletedslpckg_component(CompleteDSLPckg_Component completedslpckg_component) {
        this.completedslpckg_component = completedslpckg_component;
    }
    public CompleteDSLPckg_Property getCompletedslpckg_property() {
        return completedslpckg_property;
    }

    public void setCompletedslpckg_property(CompleteDSLPckg_Property completedslpckg_property) {
        this.completedslpckg_property = completedslpckg_property;
    }
    public CompleteDSLPckg_Component getCompletedslpckg_component() {
        return completedslpckg_component;
    }

    public void setCompletedslpckg_component(CompleteDSLPckg_Component completedslpckg_component) {
        this.completedslpckg_component = completedslpckg_component;
    }
    public List<CompleteDSLPckg_Interface> getCompletedslpckg_interfaces() {
        return completedslpckg_interfaces;
    }

    public void addCompletedslpckg_interface(Completedslpckg_interface completedslpckg_interface) {
        this.completedslpckg_interfaces.add(completedslpckg_interface);
    }
    public CompleteDSLPckg_Classifier getCompletedslpckg_classifier() {
        return completedslpckg_classifier;
    }

    public void setCompletedslpckg_classifier(CompleteDSLPckg_Classifier completedslpckg_classifier) {
        this.completedslpckg_classifier = completedslpckg_classifier;
    }

}