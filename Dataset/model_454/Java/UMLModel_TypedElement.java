





import java.util.List;
import java.util.ArrayList;

public class UMLModel_TypedElement extends NamedElement {

    private String type;



    public UMLModel_TypedElement(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}