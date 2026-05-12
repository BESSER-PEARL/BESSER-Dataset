





import java.util.List;
import java.util.ArrayList;

public class sql_OpFList extends OpFunctionArg {






    private List<sql_OpFunctionArgOperand> sql_opfunctionargoperands;


    public sql_OpFList(
    ) {
        super(
        );
        this.sql_opfunctionargoperands = new ArrayList<>();
    }

    public sql_OpFList(
        ArrayList<sql_OpFunctionArgOperand> sql_opfunctionargoperands    ) {
        this.sql_opfunctionargoperands = sql_opfunctionargoperands;
    }


    public List<sql_OpFunctionArgOperand> getSql_opfunctionargoperands() {
        return sql_opfunctionargoperands;
    }

    public void addSql_opfunctionargoperand(Sql_opfunctionargoperand sql_opfunctionargoperand) {
        this.sql_opfunctionargoperands.add(sql_opfunctionargoperand);
    }

}