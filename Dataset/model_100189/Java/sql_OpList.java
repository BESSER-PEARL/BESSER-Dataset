





import java.util.List;
import java.util.ArrayList;

public class sql_OpList extends OperandList {






    private List<sql_ScalarOperand> sql_scalaroperands;


    public sql_OpList(
    ) {
        super(
        );
        this.sql_scalaroperands = new ArrayList<>();
    }

    public sql_OpList(
        ArrayList<sql_ScalarOperand> sql_scalaroperands    ) {
        this.sql_scalaroperands = sql_scalaroperands;
    }


    public List<sql_ScalarOperand> getSql_scalaroperands() {
        return sql_scalaroperands;
    }

    public void addSql_scalaroperand(Sql_scalaroperand sql_scalaroperand) {
        this.sql_scalaroperands.add(sql_scalaroperand);
    }

}