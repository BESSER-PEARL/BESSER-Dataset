





import java.util.List;
import java.util.ArrayList;

public class idl_ShiftExpr  {

    private String op;





    private idl_AndExpr idl_andexpr;




    private idl_ShiftExpr idl_shiftexpr;


    public idl_ShiftExpr(
        String op    ) {
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public idl_AndExpr getIdl_andexpr() {
        return idl_andexpr;
    }

    public void setIdl_andexpr(idl_AndExpr idl_andexpr) {
        this.idl_andexpr = idl_andexpr;
    }
    public idl_ShiftExpr getIdl_shiftexpr() {
        return idl_shiftexpr;
    }

    public void setIdl_shiftexpr(idl_ShiftExpr idl_shiftexpr) {
        this.idl_shiftexpr = idl_shiftexpr;
    }

}