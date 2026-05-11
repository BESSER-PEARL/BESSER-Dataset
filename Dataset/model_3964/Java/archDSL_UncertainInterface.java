





import java.util.List;
import java.util.ArrayList;

public class archDSL_UncertainInterface  {

    private String name;





    private archDSL_Model archdsl_model;




    private archDSL_Interface archdsl_interface;


    public archDSL_UncertainInterface(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public archDSL_Model getArchdsl_model() {
        return archdsl_model;
    }

    public void setArchdsl_model(archDSL_Model archdsl_model) {
        this.archdsl_model = archdsl_model;
    }
    public archDSL_Interface getArchdsl_interface() {
        return archdsl_interface;
    }

    public void setArchdsl_interface(archDSL_Interface archdsl_interface) {
        this.archdsl_interface = archdsl_interface;
    }

}