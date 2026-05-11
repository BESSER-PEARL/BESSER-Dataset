





import java.util.List;
import java.util.ArrayList;

public class myDsl_assign_op  {

    private String aDD_OP;
    private String mUL_OP;





    private myDsl_SimpleStmtLinha mydsl_simplestmtlinha;


    public myDsl_assign_op(
        String aDD_OP,        String mUL_OP    ) {
        this.aDD_OP = aDD_OP;
        this.mUL_OP = mUL_OP;
    }


    public String getAdd_op() {
        return aDD_OP;
    }

    public void setAdd_op(String aDD_OP) {
        this.aDD_OP = aDD_OP;
    }
    public String getMul_op() {
        return mUL_OP;
    }

    public void setMul_op(String mUL_OP) {
        this.mUL_OP = mUL_OP;
    }

    public myDsl_SimpleStmtLinha getMydsl_simplestmtlinha() {
        return mydsl_simplestmtlinha;
    }

    public void setMydsl_simplestmtlinha(myDsl_SimpleStmtLinha mydsl_simplestmtlinha) {
        this.mydsl_simplestmtlinha = mydsl_simplestmtlinha;
    }

}