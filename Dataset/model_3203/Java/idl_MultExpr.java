





import java.util.List;
import java.util.ArrayList;

public class idl_MultExpr  {

    private String op;





    private idl_MultExpr idl_multexpr;




    private idl_AddExpr idl_addexpr;


    public idl_MultExpr(
        String op    ) {
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public idl_MultExpr getIdl_multexpr() {
        return idl_multexpr;
    }

    public void setIdl_multexpr(idl_MultExpr idl_multexpr) {
        this.idl_multexpr = idl_multexpr;
    }
    public idl_AddExpr getIdl_addexpr() {
        return idl_addexpr;
    }

    public void setIdl_addexpr(idl_AddExpr idl_addexpr) {
        this.idl_addexpr = idl_addexpr;
    }

}