





import java.util.List;
import java.util.ArrayList;

public class core_Variable extends IdentifiedElement {

    private String type;





    private core_EObject core_eobject;


    public core_Variable(
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

    public core_EObject getCore_eobject() {
        return core_eobject;
    }

    public void setCore_eobject(core_EObject core_eobject) {
        this.core_eobject = core_eobject;
    }

}