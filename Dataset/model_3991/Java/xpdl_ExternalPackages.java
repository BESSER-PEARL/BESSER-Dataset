





import java.util.List;
import java.util.ArrayList;

public class xpdl_ExternalPackages  {






    private List<xpdl_ExternalPackage> xpdl_externalpackages;


    public xpdl_ExternalPackages(
    ) {
        this.xpdl_externalpackages = new ArrayList<>();
    }

    public xpdl_ExternalPackages(
        ArrayList<xpdl_ExternalPackage> xpdl_externalpackages    ) {
        this.xpdl_externalpackages = xpdl_externalpackages;
    }


    public List<xpdl_ExternalPackage> getXpdl_externalpackages() {
        return xpdl_externalpackages;
    }

    public void addXpdl_externalpackage(Xpdl_externalpackage xpdl_externalpackage) {
        this.xpdl_externalpackages.add(xpdl_externalpackage);
    }

}