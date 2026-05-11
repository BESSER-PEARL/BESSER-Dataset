





import java.util.List;
import java.util.ArrayList;

public class sql_FunctionExtract  {

    private String v;





    private sql_Operands sql_operands;




    private sql_Operand sql_operand;


    public sql_FunctionExtract(
        String v    ) {
        this.v = v;
    }


    public String getV() {
        return v;
    }

    public void setV(String v) {
        this.v = v;
    }

    public sql_Operands getSql_operands() {
        return sql_operands;
    }

    public void setSql_operands(sql_Operands sql_operands) {
        this.sql_operands = sql_operands;
    }
    public sql_Operand getSql_operand() {
        return sql_operand;
    }

    public void setSql_operand(sql_Operand sql_operand) {
        this.sql_operand = sql_operand;
    }

}