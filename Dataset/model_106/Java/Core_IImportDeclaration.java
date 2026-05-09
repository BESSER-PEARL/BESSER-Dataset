





import java.util.List;
import java.util.ArrayList;

public class Core_IImportDeclaration extends ISourceReference, IJavaElement {

    private String isOnDemand;
    private String isStatic;



    public Core_IImportDeclaration(
        String isOnDemand,        String isStatic    ) {
        super(
        );
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