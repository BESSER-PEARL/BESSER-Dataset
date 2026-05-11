





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedOperation extends uml_TracedTemplateableElement, uml_TracedParameterableElement, uml_TracedBehavioralFeature {






    private uml_TracedType uml_tracedtype;




    private List<uml_TracedOperation> uml_tracedoperations;




    private uml_TracedClass uml_tracedclass;




    private uml_TracedConstraint uml_tracedconstraint;




    private List<uml_TracedConstraint> uml_tracedconstraints;




    private List<uml_TracedConstraint> uml_tracedconstraints;




    private uml_TracedInterface uml_tracedinterface;




    private uml_TracedDataType uml_traceddatatype;


    public umlTrace_uml_TracedOperation(
    ) {
        super(
        );
        this.uml_tracedoperations = new ArrayList<>();
        this.uml_tracedconstraints = new ArrayList<>();
        this.uml_tracedconstraints = new ArrayList<>();
    }

    public umlTrace_uml_TracedOperation(
        ArrayList<uml_TracedOperation> uml_tracedoperations,        ArrayList<uml_TracedConstraint> uml_tracedconstraints,        ArrayList<uml_TracedConstraint> uml_tracedconstraints    ) {
        this.uml_tracedoperations = uml_tracedoperations;
        this.uml_tracedconstraints = uml_tracedconstraints;
        this.uml_tracedconstraints = uml_tracedconstraints;
    }


    public uml_TracedType getUml_tracedtype() {
        return uml_tracedtype;
    }

    public void setUml_tracedtype(uml_TracedType uml_tracedtype) {
        this.uml_tracedtype = uml_tracedtype;
    }
    public List<uml_TracedOperation> getUml_tracedoperations() {
        return uml_tracedoperations;
    }

    public void addUml_tracedoperation(Uml_tracedoperation uml_tracedoperation) {
        this.uml_tracedoperations.add(uml_tracedoperation);
    }
    public uml_TracedClass getUml_tracedclass() {
        return uml_tracedclass;
    }

    public void setUml_tracedclass(uml_TracedClass uml_tracedclass) {
        this.uml_tracedclass = uml_tracedclass;
    }
    public uml_TracedConstraint getUml_tracedconstraint() {
        return uml_tracedconstraint;
    }

    public void setUml_tracedconstraint(uml_TracedConstraint uml_tracedconstraint) {
        this.uml_tracedconstraint = uml_tracedconstraint;
    }
    public List<uml_TracedConstraint> getUml_tracedconstraints() {
        return uml_tracedconstraints;
    }

    public void addUml_tracedconstraint(Uml_tracedconstraint uml_tracedconstraint) {
        this.uml_tracedconstraints.add(uml_tracedconstraint);
    }
    public List<uml_TracedConstraint> getUml_tracedconstraints() {
        return uml_tracedconstraints;
    }

    public void addUml_tracedconstraint(Uml_tracedconstraint uml_tracedconstraint) {
        this.uml_tracedconstraints.add(uml_tracedconstraint);
    }
    public uml_TracedInterface getUml_tracedinterface() {
        return uml_tracedinterface;
    }

    public void setUml_tracedinterface(uml_TracedInterface uml_tracedinterface) {
        this.uml_tracedinterface = uml_tracedinterface;
    }
    public uml_TracedDataType getUml_traceddatatype() {
        return uml_traceddatatype;
    }

    public void setUml_traceddatatype(uml_TracedDataType uml_traceddatatype) {
        this.uml_traceddatatype = uml_traceddatatype;
    }

}