





import java.util.List;
import java.util.ArrayList;

public class sql_OpFunctionCast  {

    private String p2;
    private String type;
    private String p;





    private sql_Operands sql_operands;




    private sql_LikeOperand sql_likeoperand;


    public sql_OpFunctionCast(
        String p2,        String type,        String p    ) {
        this.p2 = p2;
        this.type = type;
        this.p = p;
    }


    public String getP2() {
        return p2;
    }

    public void setP2(String p2) {
        this.p2 = p2;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getP() {
        return p;
    }

    public void setP(String p) {
        this.p = p;
    }

    public sql_Operands getSql_operands() {
        return sql_operands;
    }

    public void setSql_operands(sql_Operands sql_operands) {
        this.sql_operands = sql_operands;
    }
    public sql_LikeOperand getSql_likeoperand() {
        return sql_likeoperand;
    }

    public void setSql_likeoperand(sql_LikeOperand sql_likeoperand) {
        this.sql_likeoperand = sql_likeoperand;
    }

}