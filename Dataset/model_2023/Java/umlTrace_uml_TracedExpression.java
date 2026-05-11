





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedExpression extends TracedValueSpecification {






    private List<uml_TracedValueSpecification> uml_tracedvaluespecifications;


    public umlTrace_uml_TracedExpression(
    ) {
        super(
        );
        this.uml_tracedvaluespecifications = new ArrayList<>();
    }

    public umlTrace_uml_TracedExpression(
        ArrayList<uml_TracedValueSpecification> uml_tracedvaluespecifications    ) {
        this.uml_tracedvaluespecifications = uml_tracedvaluespecifications;
    }


    public List<uml_TracedValueSpecification> getUml_tracedvaluespecifications() {
        return uml_tracedvaluespecifications;
    }

    public void addUml_tracedvaluespecification(Uml_tracedvaluespecification uml_tracedvaluespecification) {
        this.uml_tracedvaluespecifications.add(uml_tracedvaluespecification);
    }

}