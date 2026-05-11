





import java.util.List;
import java.util.ArrayList;

public class xpdl_TypeDeclarationsType  {






    private List<xpdl_TypeDeclarationType> xpdl_typedeclarationtypes;


    public xpdl_TypeDeclarationsType(
    ) {
        this.xpdl_typedeclarationtypes = new ArrayList<>();
    }

    public xpdl_TypeDeclarationsType(
        ArrayList<xpdl_TypeDeclarationType> xpdl_typedeclarationtypes    ) {
        this.xpdl_typedeclarationtypes = xpdl_typedeclarationtypes;
    }


    public List<xpdl_TypeDeclarationType> getXpdl_typedeclarationtypes() {
        return xpdl_typedeclarationtypes;
    }

    public void addXpdl_typedeclarationtype(Xpdl_typedeclarationtype xpdl_typedeclarationtype) {
        this.xpdl_typedeclarationtypes.add(xpdl_typedeclarationtype);
    }

}