





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Transition extends RedefinableElement, Namespace {

    private String source;
    private String redefinedTransition;
    private String container;
    private String kind;
    private String target;
    private String guard;





    private List<UMLModel_Trigger> umlmodel_triggers;


    public UMLModel_Transition(
        String source,        String redefinedTransition,        String container,        String kind,        String target,        String guard    ) {
        super(
        );
        this.source = source;
        this.redefinedTransition = redefinedTransition;
        this.container = container;
        this.kind = kind;
        this.target = target;
        this.guard = guard;
        this.umlmodel_triggers = new ArrayList<>();
    }

    public UMLModel_Transition(
        String source,        String redefinedTransition,        String container,        String kind,        String target,        String guard        ArrayList<UMLModel_Trigger> umlmodel_triggers    ) {
        this.source = source;
        this.redefinedTransition = redefinedTransition;
        this.container = container;
        this.kind = kind;
        this.target = target;
        this.guard = guard;
        this.umlmodel_triggers = umlmodel_triggers;
    }

    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getRedefinedtransition() {
        return redefinedTransition;
    }

    public void setRedefinedtransition(String redefinedTransition) {
        this.redefinedTransition = redefinedTransition;
    }
    public String getContainer() {
        return container;
    }

    public void setContainer(String container) {
        this.container = container;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getGuard() {
        return guard;
    }

    public void setGuard(String guard) {
        this.guard = guard;
    }

    public List<UMLModel_Trigger> getUmlmodel_triggers() {
        return umlmodel_triggers;
    }

    public void addUmlmodel_trigger(Umlmodel_trigger umlmodel_trigger) {
        this.umlmodel_triggers.add(umlmodel_trigger);
    }

}