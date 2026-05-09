





import java.util.List;
import java.util.ArrayList;

public class iTrace_Model extends Artefact {

    private String metamodel;





    private List<iTrace_TraceLinkElement> itrace_tracelinkelements;




    private iTrace_TraceLinkElement itrace_tracelinkelement;


    public iTrace_Model(
        String metamodel    ) {
        super(
        );
        this.metamodel = metamodel;
        this.itrace_tracelinkelements = new ArrayList<>();
    }

    public iTrace_Model(
        String metamodel        ArrayList<iTrace_TraceLinkElement> itrace_tracelinkelements    ) {
        this.metamodel = metamodel;
        this.itrace_tracelinkelements = itrace_tracelinkelements;
    }

    public String getMetamodel() {
        return metamodel;
    }

    public void setMetamodel(String metamodel) {
        this.metamodel = metamodel;
    }

    public List<iTrace_TraceLinkElement> getItrace_tracelinkelements() {
        return itrace_tracelinkelements;
    }

    public void addItrace_tracelinkelement(Itrace_tracelinkelement itrace_tracelinkelement) {
        this.itrace_tracelinkelements.add(itrace_tracelinkelement);
    }
    public iTrace_TraceLinkElement getItrace_tracelinkelement() {
        return itrace_tracelinkelement;
    }

    public void setItrace_tracelinkelement(iTrace_TraceLinkElement itrace_tracelinkelement) {
        this.itrace_tracelinkelement = itrace_tracelinkelement;
    }

}