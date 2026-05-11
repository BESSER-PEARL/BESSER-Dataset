





import java.util.List;
import java.util.ArrayList;

public class idl_ParamTypeSpec extends OpTypeDecl {






    private idl_AttrDecl idl_attrdecl;




    private idl_ParamDcl idl_paramdcl;


    public idl_ParamTypeSpec(
    ) {
        super(
        );
    }



    public idl_AttrDecl getIdl_attrdecl() {
        return idl_attrdecl;
    }

    public void setIdl_attrdecl(idl_AttrDecl idl_attrdecl) {
        this.idl_attrdecl = idl_attrdecl;
    }
    public idl_ParamDcl getIdl_paramdcl() {
        return idl_paramdcl;
    }

    public void setIdl_paramdcl(idl_ParamDcl idl_paramdcl) {
        this.idl_paramdcl = idl_paramdcl;
    }

}