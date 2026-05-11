





import java.util.List;
import java.util.ArrayList;

public class xpdl1_ExternalPackagesType  {






    private List<xpdl1_ExternalPackageType> xpdl1_externalpackagetypes;




    private xpdl1_DocumentRoot xpdl1_documentroot;


    public xpdl1_ExternalPackagesType(
    ) {
        this.xpdl1_externalpackagetypes = new ArrayList<>();
    }

    public xpdl1_ExternalPackagesType(
        ArrayList<xpdl1_ExternalPackageType> xpdl1_externalpackagetypes    ) {
        this.xpdl1_externalpackagetypes = xpdl1_externalpackagetypes;
    }


    public List<xpdl1_ExternalPackageType> getXpdl1_externalpackagetypes() {
        return xpdl1_externalpackagetypes;
    }

    public void addXpdl1_externalpackagetype(Xpdl1_externalpackagetype xpdl1_externalpackagetype) {
        this.xpdl1_externalpackagetypes.add(xpdl1_externalpackagetype);
    }
    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }

}