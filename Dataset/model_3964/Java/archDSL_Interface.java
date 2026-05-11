





import java.util.List;
import java.util.ArrayList;

public class archDSL_Interface  {

    private String name;





    private archDSL_Model archdsl_model;


    public archDSL_Interface(
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

}