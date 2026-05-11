





import java.util.List;
import java.util.ArrayList;

public class sql_OperandListGroup  {






    private sql_ExistsOper sql_existsoper;




    private sql_InOper sql_inoper;


    public sql_OperandListGroup(
    ) {
    }



    public sql_ExistsOper getSql_existsoper() {
        return sql_existsoper;
    }

    public void setSql_existsoper(sql_ExistsOper sql_existsoper) {
        this.sql_existsoper = sql_existsoper;
    }
    public sql_InOper getSql_inoper() {
        return sql_inoper;
    }

    public void setSql_inoper(sql_InOper sql_inoper) {
        this.sql_inoper = sql_inoper;
    }

}