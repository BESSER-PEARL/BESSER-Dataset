





import java.util.List;
import java.util.ArrayList;

public class idl_OrExpr extends ConstExp {

    private String op;





    private idl_OrExpr idl_orexpr;


    public idl_OrExpr(
        String op    ) {
        super(
        );
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public idl_OrExpr getIdl_orexpr() {
        return idl_orexpr;
    }

    public void setIdl_orexpr(idl_OrExpr idl_orexpr) {
        this.idl_orexpr = idl_orexpr;
    }

}