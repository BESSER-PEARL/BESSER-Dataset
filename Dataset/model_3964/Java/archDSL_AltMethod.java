





import java.util.List;
import java.util.ArrayList;

public class archDSL_AltMethod extends SuperMethod {

    private String type;
    private String a_name;





    private archDSL_UncertainInterface archdsl_uncertaininterface;


    public archDSL_AltMethod(
        String type,        String a_name    ) {
        super(
        );
        this.type = type;
        this.a_name = a_name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getA_name() {
        return a_name;
    }

    public void setA_name(String a_name) {
        this.a_name = a_name;
    }

    public archDSL_UncertainInterface getArchdsl_uncertaininterface() {
        return archdsl_uncertaininterface;
    }

    public void setArchdsl_uncertaininterface(archDSL_UncertainInterface archdsl_uncertaininterface) {
        this.archdsl_uncertaininterface = archdsl_uncertaininterface;
    }

}