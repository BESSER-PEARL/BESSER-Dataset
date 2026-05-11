





import java.util.List;
import java.util.ArrayList;

public class UML_Parameter extends TypedElement {

    private String direction;





    private UML_Operation uml_operation;


    public UML_Parameter(
        String direction    ) {
        super(
        );
        this.direction = direction;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }

    public UML_Operation getUml_operation() {
        return uml_operation;
    }

    public void setUml_operation(UML_Operation uml_operation) {
        this.uml_operation = uml_operation;
    }

}