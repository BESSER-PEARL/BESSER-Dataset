





import java.util.List;
import java.util.ArrayList;

public class archDSL_OptMethod extends SuperMethod {

    private String type;





    private archDSL_UncertainInterface archdsl_uncertaininterface;


    public archDSL_OptMethod(
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

    public archDSL_UncertainInterface getArchdsl_uncertaininterface() {
        return archdsl_uncertaininterface;
    }

    public void setArchdsl_uncertaininterface(archDSL_UncertainInterface archdsl_uncertaininterface) {
        this.archdsl_uncertaininterface = archdsl_uncertaininterface;
    }

}