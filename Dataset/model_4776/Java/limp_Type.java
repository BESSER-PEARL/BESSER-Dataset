





import java.util.List;
import java.util.ArrayList;

public class limp_Type  {






    private limp_ArrayTypeDef limp_arraytypedef;




    private limp_ConstantDeclaration limp_constantdeclaration;




    private limp_GlobalDeclaration limp_globaldeclaration;




    private limp_OutputArg limp_outputarg;


    public limp_Type(
    ) {
    }



    public limp_ArrayTypeDef getLimp_arraytypedef() {
        return limp_arraytypedef;
    }

    public void setLimp_arraytypedef(limp_ArrayTypeDef limp_arraytypedef) {
        this.limp_arraytypedef = limp_arraytypedef;
    }
    public limp_ConstantDeclaration getLimp_constantdeclaration() {
        return limp_constantdeclaration;
    }

    public void setLimp_constantdeclaration(limp_ConstantDeclaration limp_constantdeclaration) {
        this.limp_constantdeclaration = limp_constantdeclaration;
    }
    public limp_GlobalDeclaration getLimp_globaldeclaration() {
        return limp_globaldeclaration;
    }

    public void setLimp_globaldeclaration(limp_GlobalDeclaration limp_globaldeclaration) {
        this.limp_globaldeclaration = limp_globaldeclaration;
    }
    public limp_OutputArg getLimp_outputarg() {
        return limp_outputarg;
    }

    public void setLimp_outputarg(limp_OutputArg limp_outputarg) {
        this.limp_outputarg = limp_outputarg;
    }

}