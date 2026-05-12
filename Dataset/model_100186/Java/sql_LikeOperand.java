





import java.util.List;
import java.util.ArrayList;

public class sql_LikeOperand  {

    private String op2;





    private sql_POperand sql_poperand;




    private sql_OpFunction sql_opfunction;




    private sql_OpFunctionCast sql_opfunctioncast;




    private sql_Like sql_like;


    public sql_LikeOperand(
        String op2    ) {
        this.op2 = op2;
    }


    public String getOp2() {
        return op2;
    }

    public void setOp2(String op2) {
        this.op2 = op2;
    }

    public sql_POperand getSql_poperand() {
        return sql_poperand;
    }

    public void setSql_poperand(sql_POperand sql_poperand) {
        this.sql_poperand = sql_poperand;
    }
    public sql_OpFunction getSql_opfunction() {
        return sql_opfunction;
    }

    public void setSql_opfunction(sql_OpFunction sql_opfunction) {
        this.sql_opfunction = sql_opfunction;
    }
    public sql_OpFunctionCast getSql_opfunctioncast() {
        return sql_opfunctioncast;
    }

    public void setSql_opfunctioncast(sql_OpFunctionCast sql_opfunctioncast) {
        this.sql_opfunctioncast = sql_opfunctioncast;
    }
    public sql_Like getSql_like() {
        return sql_like;
    }

    public void setSql_like(sql_Like sql_like) {
        this.sql_like = sql_like;
    }

}