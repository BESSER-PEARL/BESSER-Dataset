





import java.util.List;
import java.util.ArrayList;

public class Core_IImportDeclaration extends IJavaElement, ISourceReference {

    private String isStatic;
    private String isOnDemand;



    public Core_IImportDeclaration(
        String isStatic,        String isOnDemand    ) {
        super(
        );
        this.isStatic = isStatic;
        this.isOnDemand = isOnDemand;
    }


    public String getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(String isStatic) {
        this.isStatic = isStatic;
    }
    public String getIsondemand() {
        return isOnDemand;
    }

    public void setIsondemand(String isOnDemand) {
        this.isOnDemand = isOnDemand;
    }


}