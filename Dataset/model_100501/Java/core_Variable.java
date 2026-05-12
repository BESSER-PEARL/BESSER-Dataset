





import java.util.List;
import java.util.ArrayList;

public class core_Variable extends IdentifiedElement {

    private String type;





    private core_SystemContext core_systemcontext;


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

    public core_SystemContext getCore_systemcontext() {
        return core_systemcontext;
    }

    public void setCore_systemcontext(core_SystemContext core_systemcontext) {
        this.core_systemcontext = core_systemcontext;
    }

}