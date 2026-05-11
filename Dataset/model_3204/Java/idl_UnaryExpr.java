





import java.util.List;
import java.util.ArrayList;

public class idl_UnaryExpr  {

    private String op;





    private idl_MultExpr idl_multexpr;


    public idl_UnaryExpr(
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

}