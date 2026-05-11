





import java.util.List;
import java.util.ArrayList;

public class vcml_Import  {

    private String importURI;





    private vcml_VcmlModel vcml_vcmlmodel;


    public vcml_Import(
        String importURI    ) {
        this.importURI = importURI;
    }


    public String getImporturi() {
        return importURI;
    }

    public void setImporturi(String importURI) {
        this.importURI = importURI;
    }

    public vcml_VcmlModel getVcml_vcmlmodel() {
        return vcml_vcmlmodel;
    }

    public void setVcml_vcmlmodel(vcml_VcmlModel vcml_vcmlmodel) {
        this.vcml_vcmlmodel = vcml_vcmlmodel;
    }

}