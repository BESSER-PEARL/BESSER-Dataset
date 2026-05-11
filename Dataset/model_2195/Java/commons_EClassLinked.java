





import java.util.List;
import java.util.ArrayList;

public class commons_EClassLinked  {

    private String eClassName;
    private String eClassStatus;
    private String ePackageName;
    private String ePackageNsPrefix;



    public commons_EClassLinked(
        String eClassName,        String eClassStatus,        String ePackageName,        String ePackageNsPrefix    ) {
        this.eClassName = eClassName;
        this.eClassStatus = eClassStatus;
        this.ePackageName = ePackageName;
        this.ePackageNsPrefix = ePackageNsPrefix;
    }


    public String getEclassname() {
        return eClassName;
    }

    public void setEclassname(String eClassName) {
        this.eClassName = eClassName;
    }
    public String getEclassstatus() {
        return eClassStatus;
    }

    public void setEclassstatus(String eClassStatus) {
        this.eClassStatus = eClassStatus;
    }
    public String getEpackagename() {
        return ePackageName;
    }

    public void setEpackagename(String ePackageName) {
        this.ePackageName = ePackageName;
    }
    public String getEpackagensprefix() {
        return ePackageNsPrefix;
    }

    public void setEpackagensprefix(String ePackageNsPrefix) {
        this.ePackageNsPrefix = ePackageNsPrefix;
    }


}