





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedLinkEndData extends TracedElement {






    private List<uml_TracedQualifierValue> uml_tracedqualifiervalues;




    private uml_TracedInputPin uml_tracedinputpin;




    private uml_TracedProperty uml_tracedproperty;


    public umlTrace_uml_TracedLinkEndData(
    ) {
        super(
        );
        this.uml_tracedqualifiervalues = new ArrayList<>();
    }

    public umlTrace_uml_TracedLinkEndData(
        ArrayList<uml_TracedQualifierValue> uml_tracedqualifiervalues    ) {
        this.uml_tracedqualifiervalues = uml_tracedqualifiervalues;
    }


    public List<uml_TracedQualifierValue> getUml_tracedqualifiervalues() {
        return uml_tracedqualifiervalues;
    }

    public void addUml_tracedqualifiervalue(Uml_tracedqualifiervalue uml_tracedqualifiervalue) {
        this.uml_tracedqualifiervalues.add(uml_tracedqualifiervalue);
    }
    public uml_TracedInputPin getUml_tracedinputpin() {
        return uml_tracedinputpin;
    }

    public void setUml_tracedinputpin(uml_TracedInputPin uml_tracedinputpin) {
        this.uml_tracedinputpin = uml_tracedinputpin;
    }
    public uml_TracedProperty getUml_tracedproperty() {
        return uml_tracedproperty;
    }

    public void setUml_tracedproperty(uml_TracedProperty uml_tracedproperty) {
        this.uml_tracedproperty = uml_tracedproperty;
    }

}