





import java.util.List;
import java.util.ArrayList;

public class sql_OpFunction  {

    private String fname;





    private sql_LikeOperand sql_likeoperand;




    private sql_Operand sql_operand;


    public sql_OpFunction(
        String fname    ) {
        this.fname = fname;
    }


    public String getFname() {
        return fname;
    }

    public void setFname(String fname) {
        this.fname = fname;
    }

    public sql_LikeOperand getSql_likeoperand() {
        return sql_likeoperand;
    }

    public void setSql_likeoperand(sql_LikeOperand sql_likeoperand) {
        this.sql_likeoperand = sql_likeoperand;
    }
    public sql_Operand getSql_operand() {
        return sql_operand;
    }

    public void setSql_operand(sql_Operand sql_operand) {
        this.sql_operand = sql_operand;
    }

}