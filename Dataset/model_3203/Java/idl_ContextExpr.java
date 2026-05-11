





import java.util.List;
import java.util.ArrayList;

public class idl_ContextExpr  {

    private String literal;





    private idl_OpDecl idl_opdecl;


    public idl_ContextExpr(
        String literal    ) {
        this.literal = literal;
    }


    public String getLiteral() {
        return literal;
    }

    public void setLiteral(String literal) {
        this.literal = literal;
    }

    public idl_OpDecl getIdl_opdecl() {
        return idl_opdecl;
    }

    public void setIdl_opdecl(idl_OpDecl idl_opdecl) {
        this.idl_opdecl = idl_opdecl;
    }

}