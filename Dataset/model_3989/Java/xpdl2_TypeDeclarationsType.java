





import java.util.List;
import java.util.ArrayList;

public class xpdl2_TypeDeclarationsType  {






    private List<xpdl2_TypeDeclarationType> xpdl2_typedeclarationtypes;


    public xpdl2_TypeDeclarationsType(
    ) {
        this.xpdl2_typedeclarationtypes = new ArrayList<>();
    }

    public xpdl2_TypeDeclarationsType(
        ArrayList<xpdl2_TypeDeclarationType> xpdl2_typedeclarationtypes    ) {
        this.xpdl2_typedeclarationtypes = xpdl2_typedeclarationtypes;
    }


    public List<xpdl2_TypeDeclarationType> getXpdl2_typedeclarationtypes() {
        return xpdl2_typedeclarationtypes;
    }

    public void addXpdl2_typedeclarationtype(Xpdl2_typedeclarationtype xpdl2_typedeclarationtype) {
        this.xpdl2_typedeclarationtypes.add(xpdl2_typedeclarationtype);
    }

}