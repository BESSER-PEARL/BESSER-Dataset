





import java.util.List;
import java.util.ArrayList;

public class uml_ConnectableElement extends TypedElement, ParameterableElement {






    private uml_Lifeline uml_lifeline;


    public uml_ConnectableElement(
    ) {
        super(
        );
    }



    public uml_Lifeline getUml_lifeline() {
        return uml_lifeline;
    }

    public void setUml_lifeline(uml_Lifeline uml_lifeline) {
        this.uml_lifeline = uml_lifeline;
    }

}