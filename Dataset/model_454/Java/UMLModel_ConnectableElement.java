





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ConnectableElement extends ParameterableElement, TypedElement {

    private String end;



    public UMLModel_ConnectableElement(
        String end    ) {
        super(
        );
        this.end = end;
    }


    public String getEnd() {
        return end;
    }

    public void setEnd(String end) {
        this.end = end;
    }


}