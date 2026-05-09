





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Port extends Property {

    private boolean isService;
    private boolean isBehavior;
    private boolean isConjugated;





    private List<CompleteDSLPckg_Interface> completedslpckg_interfaces;




    private List<CompleteDSLPckg_Interface> completedslpckg_interfaces;




    private CompleteDSLPckg_Port completedslpckg_port;




    private CompleteDSLPckg_EncapsulatedClassifier completedslpckg_encapsulatedclassifier;


    public CompleteDSLPckg_Port(
        boolean isService,        boolean isBehavior,        boolean isConjugated    ) {
        super(
        );
        this.isService = isService;
        this.isBehavior = isBehavior;
        this.isConjugated = isConjugated;
        this.completedslpckg_interfaces = new ArrayList<>();
        this.completedslpckg_interfaces = new ArrayList<>();
    }

    public CompleteDSLPckg_Port(
        boolean isService,        boolean isBehavior,        boolean isConjugated        ArrayList<CompleteDSLPckg_Interface> completedslpckg_interfaces,        ArrayList<CompleteDSLPckg_Interface> completedslpckg_interfaces    ) {
        this.isService = isService;
        this.isBehavior = isBehavior;
        this.isConjugated = isConjugated;
        this.completedslpckg_interfaces = completedslpckg_interfaces;
        this.completedslpckg_interfaces = completedslpckg_interfaces;
    }

    public boolean getIsservice() {
        return isService;
    }

    public void setIsservice(boolean isService) {
        this.isService = isService;
    }
    public boolean getIsbehavior() {
        return isBehavior;
    }

    public void setIsbehavior(boolean isBehavior) {
        this.isBehavior = isBehavior;
    }
    public boolean getIsconjugated() {
        return isConjugated;
    }

    public void setIsconjugated(boolean isConjugated) {
        this.isConjugated = isConjugated;
    }

    public List<CompleteDSLPckg_Interface> getCompletedslpckg_interfaces() {
        return completedslpckg_interfaces;
    }

    public void addCompletedslpckg_interface(Completedslpckg_interface completedslpckg_interface) {
        this.completedslpckg_interfaces.add(completedslpckg_interface);
    }
    public List<CompleteDSLPckg_Interface> getCompletedslpckg_interfaces() {
        return completedslpckg_interfaces;
    }

    public void addCompletedslpckg_interface(Completedslpckg_interface completedslpckg_interface) {
        this.completedslpckg_interfaces.add(completedslpckg_interface);
    }
    public CompleteDSLPckg_Port getCompletedslpckg_port() {
        return completedslpckg_port;
    }

    public void setCompletedslpckg_port(CompleteDSLPckg_Port completedslpckg_port) {
        this.completedslpckg_port = completedslpckg_port;
    }
    public CompleteDSLPckg_EncapsulatedClassifier getCompletedslpckg_encapsulatedclassifier() {
        return completedslpckg_encapsulatedclassifier;
    }

    public void setCompletedslpckg_encapsulatedclassifier(CompleteDSLPckg_EncapsulatedClassifier completedslpckg_encapsulatedclassifier) {
        this.completedslpckg_encapsulatedclassifier = completedslpckg_encapsulatedclassifier;
    }

}