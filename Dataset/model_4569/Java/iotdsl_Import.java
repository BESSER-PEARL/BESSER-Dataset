





import java.util.List;
import java.util.ArrayList;

public class iotdsl_Import  {

    private String importedNamespace;





    private iotdsl_IotModel iotdsl_iotmodel;


    public iotdsl_Import(
        String importedNamespace    ) {
        this.importedNamespace = importedNamespace;
    }


    public String getImportednamespace() {
        return importedNamespace;
    }

    public void setImportednamespace(String importedNamespace) {
        this.importedNamespace = importedNamespace;
    }

    public iotdsl_IotModel getIotdsl_iotmodel() {
        return iotdsl_iotmodel;
    }

    public void setIotdsl_iotmodel(iotdsl_IotModel iotdsl_iotmodel) {
        this.iotdsl_iotmodel = iotdsl_iotmodel;
    }

}