





import java.util.List;
import java.util.ArrayList;

public class schema_StorySchemaCatalog extends NsPrefixable, ResourceAware, BundleAware {

    private String xmiUrl;
    private String ecoreUrl;
    private String generatedPackageName;



    public schema_StorySchemaCatalog(
        String xmiUrl,        String ecoreUrl,        String generatedPackageName    ) {
        super(
        );
        this.xmiUrl = xmiUrl;
        this.ecoreUrl = ecoreUrl;
        this.generatedPackageName = generatedPackageName;
    }


    public String getXmiurl() {
        return xmiUrl;
    }

    public void setXmiurl(String xmiUrl) {
        this.xmiUrl = xmiUrl;
    }
    public String getEcoreurl() {
        return ecoreUrl;
    }

    public void setEcoreurl(String ecoreUrl) {
        this.ecoreUrl = ecoreUrl;
    }
    public String getGeneratedpackagename() {
        return generatedPackageName;
    }

    public void setGeneratedpackagename(String generatedPackageName) {
        this.generatedPackageName = generatedPackageName;
    }


}