





import java.util.List;
import java.util.ArrayList;

public class schema_StorySchemaCatalog extends ResourceAware, BundleAware, NsPrefixable {

    private String generatedPackageName;
    private String ecoreUrl;
    private String xmiUrl;



    public schema_StorySchemaCatalog(
        String generatedPackageName,        String ecoreUrl,        String xmiUrl    ) {
        super(
        );
        this.generatedPackageName = generatedPackageName;
        this.ecoreUrl = ecoreUrl;
        this.xmiUrl = xmiUrl;
    }


    public String getGeneratedpackagename() {
        return generatedPackageName;
    }

    public void setGeneratedpackagename(String generatedPackageName) {
        this.generatedPackageName = generatedPackageName;
    }
    public String getEcoreurl() {
        return ecoreUrl;
    }

    public void setEcoreurl(String ecoreUrl) {
        this.ecoreUrl = ecoreUrl;
    }
    public String getXmiurl() {
        return xmiUrl;
    }

    public void setXmiurl(String xmiUrl) {
        this.xmiUrl = xmiUrl;
    }


}