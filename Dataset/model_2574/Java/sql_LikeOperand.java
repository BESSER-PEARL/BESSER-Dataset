





import java.util.List;
import java.util.ArrayList;

public class sql_LikeOperand  {

    private String op2;





    private sql_Like sql_like;




    private sql_OpFunction sql_opfunction;


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

    public sql_Like getSql_like() {
        return sql_like;
    }

    public void setSql_like(sql_Like sql_like) {
        this.sql_like = sql_like;
    }
    public sql_OpFunction getSql_opfunction() {
        return sql_opfunction;
    }

    public void setSql_opfunction(sql_OpFunction sql_opfunction) {
        this.sql_opfunction = sql_opfunction;
    }

}