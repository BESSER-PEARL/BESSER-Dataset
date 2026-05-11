





import java.util.List;
import java.util.ArrayList;

public class archDSL_Method extends SuperMethod {

    private String type;





    private archDSL_Interface archdsl_interface;




    private archDSL_Behavior archdsl_behavior;


    public archDSL_Method(
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

    public archDSL_Interface getArchdsl_interface() {
        return archdsl_interface;
    }

    public void setArchdsl_interface(archDSL_Interface archdsl_interface) {
        this.archdsl_interface = archdsl_interface;
    }
    public archDSL_Behavior getArchdsl_behavior() {
        return archdsl_behavior;
    }

    public void setArchdsl_behavior(archDSL_Behavior archdsl_behavior) {
        this.archdsl_behavior = archdsl_behavior;
    }

}