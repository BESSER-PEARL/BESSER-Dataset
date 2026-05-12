





import java.util.List;
import java.util.ArrayList;

public class core_Interaction extends IdentifiedElement {

    private String direction;





    private core_EObject core_eobject;


    public core_Interaction(
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

    public core_EObject getCore_eobject() {
        return core_eobject;
    }

    public void setCore_eobject(core_EObject core_eobject) {
        this.core_eobject = core_eobject;
    }

}