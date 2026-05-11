





import java.util.List;
import java.util.ArrayList;

public class idl_AddExpr  {

    private String op;





    private idl_AddExpr idl_addexpr;




    private idl_ShiftExpr idl_shiftexpr;


    public idl_AddExpr(
        String op    ) {
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public idl_AddExpr getIdl_addexpr() {
        return idl_addexpr;
    }

    public void setIdl_addexpr(idl_AddExpr idl_addexpr) {
        this.idl_addexpr = idl_addexpr;
    }
    public idl_ShiftExpr getIdl_shiftexpr() {
        return idl_shiftexpr;
    }

    public void setIdl_shiftexpr(idl_ShiftExpr idl_shiftexpr) {
        this.idl_shiftexpr = idl_shiftexpr;
    }

}