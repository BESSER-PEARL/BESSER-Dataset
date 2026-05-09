





import java.util.List;
import java.util.ArrayList;

public class fIDL_Constant  {

    private String ci;





    private fIDL_ConstDeclaration fidl_constdeclaration;


    public fIDL_Constant(
        String ci    ) {
        this.ci = ci;
    }


    public String getCi() {
        return ci;
    }

    public void setCi(String ci) {
        this.ci = ci;
    }

    public fIDL_ConstDeclaration getFidl_constdeclaration() {
        return fidl_constdeclaration;
    }

    public void setFidl_constdeclaration(fIDL_ConstDeclaration fidl_constdeclaration) {
        this.fidl_constdeclaration = fidl_constdeclaration;
    }

}