





import java.util.List;
import java.util.ArrayList;

public class sql_OpFunctionCast  {

    private String type;
    private int p2;
    private int p;





    private sql_Operands sql_operands;


    public sql_OpFunctionCast(
        String type,        int p2,        int p    ) {
        this.type = type;
        this.p2 = p2;
        this.p = p;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getP2() {
        return p2;
    }

    public void setP2(int p2) {
        this.p2 = p2;
    }
    public int getP() {
        return p;
    }

    public void setP(int p) {
        this.p = p;
    }

    public sql_Operands getSql_operands() {
        return sql_operands;
    }

    public void setSql_operands(sql_Operands sql_operands) {
        this.sql_operands = sql_operands;
    }

}