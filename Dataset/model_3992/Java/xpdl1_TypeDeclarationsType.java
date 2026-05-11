





import java.util.List;
import java.util.ArrayList;

public class xpdl1_TypeDeclarationsType  {






    private xpdl1_DocumentRoot xpdl1_documentroot;




    private List<xpdl1_TypeDeclarationType> xpdl1_typedeclarationtypes;




    private xpdl1_PackageType xpdl1_packagetype;


    public xpdl1_TypeDeclarationsType(
    ) {
        this.xpdl1_typedeclarationtypes = new ArrayList<>();
    }

    public xpdl1_TypeDeclarationsType(
        ArrayList<xpdl1_TypeDeclarationType> xpdl1_typedeclarationtypes    ) {
        this.xpdl1_typedeclarationtypes = xpdl1_typedeclarationtypes;
    }


    public xpdl1_DocumentRoot getXpdl1_documentroot() {
        return xpdl1_documentroot;
    }

    public void setXpdl1_documentroot(xpdl1_DocumentRoot xpdl1_documentroot) {
        this.xpdl1_documentroot = xpdl1_documentroot;
    }
    public List<xpdl1_TypeDeclarationType> getXpdl1_typedeclarationtypes() {
        return xpdl1_typedeclarationtypes;
    }

    public void addXpdl1_typedeclarationtype(Xpdl1_typedeclarationtype xpdl1_typedeclarationtype) {
        this.xpdl1_typedeclarationtypes.add(xpdl1_typedeclarationtype);
    }
    public xpdl1_PackageType getXpdl1_packagetype() {
        return xpdl1_packagetype;
    }

    public void setXpdl1_packagetype(xpdl1_PackageType xpdl1_packagetype) {
        this.xpdl1_packagetype = xpdl1_packagetype;
    }

}