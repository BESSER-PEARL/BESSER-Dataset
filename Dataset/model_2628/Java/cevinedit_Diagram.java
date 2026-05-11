





import java.util.List;
import java.util.ArrayList;

public class cevinedit_Diagram  {

    private String name;
    private String modelExtension;





    private cevinedit_CEViNEditRoot cevinedit_cevineditroot;


    public cevinedit_Diagram(
        String name,        String modelExtension    ) {
        this.name = name;
        this.modelExtension = modelExtension;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getModelextension() {
        return modelExtension;
    }

    public void setModelextension(String modelExtension) {
        this.modelExtension = modelExtension;
    }

    public cevinedit_CEViNEditRoot getCevinedit_cevineditroot() {
        return cevinedit_cevineditroot;
    }

    public void setCevinedit_cevineditroot(cevinedit_CEViNEditRoot cevinedit_cevineditroot) {
        this.cevinedit_cevineditroot = cevinedit_cevineditroot;
    }

}