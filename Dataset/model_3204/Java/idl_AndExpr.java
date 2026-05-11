





import java.util.List;
import java.util.ArrayList;

public class idl_AndExpr  {

    private String op;





    private idl_AndExpr idl_andexpr;




    private idl_XOrExpr idl_xorexpr;




    private idl_ShiftExpr idl_shiftexpr;


    public idl_AndExpr(
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
    public idl_XOrExpr getIdl_xorexpr() {
        return idl_xorexpr;
    }

    public void setIdl_xorexpr(idl_XOrExpr idl_xorexpr) {
        this.idl_xorexpr = idl_xorexpr;
    }
    public idl_ShiftExpr getIdl_shiftexpr() {
        return idl_shiftexpr;
    }

    public void setIdl_shiftexpr(idl_ShiftExpr idl_shiftexpr) {
        this.idl_shiftexpr = idl_shiftexpr;
    }

}