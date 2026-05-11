





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedExtend extends uml_TracedNamedElement, uml_TracedDirectedRelationship {






    private uml_TracedConstraint uml_tracedconstraint;




    private uml_TracedUseCase uml_tracedusecase;




    private List<uml_TracedExtensionPoint> uml_tracedextensionpoints;




    private uml_TracedUseCase uml_tracedusecase;


    public umlTrace_uml_TracedExtend(
    ) {
        super(
        );
        this.uml_tracedextensionpoints = new ArrayList<>();
    }

    public umlTrace_uml_TracedExtend(
        ArrayList<uml_TracedExtensionPoint> uml_tracedextensionpoints    ) {
        this.uml_tracedextensionpoints = uml_tracedextensionpoints;
    }


    public uml_TracedConstraint getUml_tracedconstraint() {
        return uml_tracedconstraint;
    }

    public void setUml_tracedconstraint(uml_TracedConstraint uml_tracedconstraint) {
        this.uml_tracedconstraint = uml_tracedconstraint;
    }
    public uml_TracedUseCase getUml_tracedusecase() {
        return uml_tracedusecase;
    }

    public void setUml_tracedusecase(uml_TracedUseCase uml_tracedusecase) {
        this.uml_tracedusecase = uml_tracedusecase;
    }
    public List<uml_TracedExtensionPoint> getUml_tracedextensionpoints() {
        return uml_tracedextensionpoints;
    }

    public void addUml_tracedextensionpoint(Uml_tracedextensionpoint uml_tracedextensionpoint) {
        this.uml_tracedextensionpoints.add(uml_tracedextensionpoint);
    }
    public uml_TracedUseCase getUml_tracedusecase() {
        return uml_tracedusecase;
    }

    public void setUml_tracedusecase(uml_TracedUseCase uml_tracedusecase) {
        this.uml_tracedusecase = uml_tracedusecase;
    }

}