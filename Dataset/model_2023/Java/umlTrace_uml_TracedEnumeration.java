





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedEnumeration extends TracedDataType {






    private List<uml_TracedEnumerationLiteral> uml_tracedenumerationliterals;


    public umlTrace_uml_TracedEnumeration(
    ) {
        super(
        );
        this.uml_tracedenumerationliterals = new ArrayList<>();
    }

    public umlTrace_uml_TracedEnumeration(
        ArrayList<uml_TracedEnumerationLiteral> uml_tracedenumerationliterals    ) {
        this.uml_tracedenumerationliterals = uml_tracedenumerationliterals;
    }


    public List<uml_TracedEnumerationLiteral> getUml_tracedenumerationliterals() {
        return uml_tracedenumerationliterals;
    }

    public void addUml_tracedenumerationliteral(Uml_tracedenumerationliteral uml_tracedenumerationliteral) {
        this.uml_tracedenumerationliterals.add(uml_tracedenumerationliteral);
    }

}