





import java.util.List;
import java.util.ArrayList;

public class dsml_DModelElementBridge  {

    private String ecoreName;
    private String ecorePath;





    private dsml_DSemanticBridge dsml_dsemanticbridge;


    public dsml_DModelElementBridge(
        String ecoreName,        String ecorePath    ) {
        this.ecoreName = ecoreName;
        this.ecorePath = ecorePath;
    }


    public String getEcorename() {
        return ecoreName;
    }

    public void setEcorename(String ecoreName) {
        this.ecoreName = ecoreName;
    }
    public String getEcorepath() {
        return ecorePath;
    }

    public void setEcorepath(String ecorePath) {
        this.ecorePath = ecorePath;
    }

    public dsml_DSemanticBridge getDsml_dsemanticbridge() {
        return dsml_dsemanticbridge;
    }

    public void setDsml_dsemanticbridge(dsml_DSemanticBridge dsml_dsemanticbridge) {
        this.dsml_dsemanticbridge = dsml_dsemanticbridge;
    }

}