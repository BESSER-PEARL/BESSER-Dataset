





import java.util.List;
import java.util.ArrayList;

public class PrimitiveTypes_Core_IImportDeclaration extends Core_IJavaElement, Core_ISourceReference {

    private String isOnDemand;
    private String isStatic;



    public PrimitiveTypes_Core_IImportDeclaration(
        String isOnDemand,        String isStatic    ) {
        super(
            String,            elementName,            String,            source        );
        this.isOnDemand = isOnDemand;
        this.isStatic = isStatic;
    }


    public String getIsondemand() {
        return isOnDemand;
    }

    public void setIsondemand(String isOnDemand) {
        this.isOnDemand = isOnDemand;
    }
    public String getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(String isStatic) {
        this.isStatic = isStatic;
    }


}