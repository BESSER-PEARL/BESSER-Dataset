





import java.util.List;
import java.util.ArrayList;

public class idl_XOrExpr  {

    private String op;





    private idl_XOrExpr idl_xorexpr;




    private idl_OrExpr idl_orexpr;


    public idl_XOrExpr(
        String op    ) {
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public idl_XOrExpr getIdl_xorexpr() {
        return idl_xorexpr;
    }

    public void setIdl_xorexpr(idl_XOrExpr idl_xorexpr) {
        this.idl_xorexpr = idl_xorexpr;
    }
    public idl_OrExpr getIdl_orexpr() {
        return idl_orexpr;
    }

    public void setIdl_orexpr(idl_OrExpr idl_orexpr) {
        this.idl_orexpr = idl_orexpr;
    }

}