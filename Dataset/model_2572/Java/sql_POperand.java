





import java.util.List;
import java.util.ArrayList;

public class sql_POperand  {

    private String prm;





    private sql_Operand sql_operand;


    public sql_POperand(
        String prm    ) {
        this.prm = prm;
    }


    public String getPrm() {
        return prm;
    }

    public void setPrm(String prm) {
        this.prm = prm;
    }

    public sql_Operand getSql_operand() {
        return sql_operand;
    }

    public void setSql_operand(sql_Operand sql_operand) {
        this.sql_operand = sql_operand;
    }

}