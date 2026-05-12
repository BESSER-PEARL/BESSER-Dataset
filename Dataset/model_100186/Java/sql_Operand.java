





import java.util.List;
import java.util.ArrayList;

public class sql_Operand  {






    private sql_SubQueryOperand sql_subqueryoperand;




    private sql_Operand sql_operand;




    private sql_Operands sql_operands;




    private sql_OpFunction sql_opfunction;




    private sql_OpFunctionCast sql_opfunctioncast;




    private sql_Operands sql_operands;




    private sql_POperand sql_poperand;


    public sql_Operand(
    ) {
    }



    public sql_SubQueryOperand getSql_subqueryoperand() {
        return sql_subqueryoperand;
    }

    public void setSql_subqueryoperand(sql_SubQueryOperand sql_subqueryoperand) {
        this.sql_subqueryoperand = sql_subqueryoperand;
    }
    public sql_Operand getSql_operand() {
        return sql_operand;
    }

    public void setSql_operand(sql_Operand sql_operand) {
        this.sql_operand = sql_operand;
    }
    public sql_Operands getSql_operands() {
        return sql_operands;
    }

    public void setSql_operands(sql_Operands sql_operands) {
        this.sql_operands = sql_operands;
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
    public sql_Operands getSql_operands() {
        return sql_operands;
    }

    public void setSql_operands(sql_Operands sql_operands) {
        this.sql_operands = sql_operands;
    }
    public sql_POperand getSql_poperand() {
        return sql_poperand;
    }

    public void setSql_poperand(sql_POperand sql_poperand) {
        this.sql_poperand = sql_poperand;
    }

}