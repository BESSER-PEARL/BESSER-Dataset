





import java.util.List;
import java.util.ArrayList;

public class UML2_Parameter extends MultiplicityElement {

    private String direction;





    private UML2_Operation uml2_operation;


    public UML2_Parameter(
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

    public UML2_Operation getUml2_operation() {
        return uml2_operation;
    }

    public void setUml2_operation(UML2_Operation uml2_operation) {
        this.uml2_operation = uml2_operation;
    }

}