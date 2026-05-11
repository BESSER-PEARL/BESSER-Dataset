





import java.util.List;
import java.util.ArrayList;

public class sql_Operands extends OpFunctionArgAgregate {






    private sql_ColumnOrAlias sql_columnoralias;




    private sql_Operands sql_operands;


    public sql_Operands(
    ) {
        super(
        );
    }



    public sql_ColumnOrAlias getSql_columnoralias() {
        return sql_columnoralias;
    }

    public void setSql_columnoralias(sql_ColumnOrAlias sql_columnoralias) {
        this.sql_columnoralias = sql_columnoralias;
    }
    public sql_Operands getSql_operands() {
        return sql_operands;
    }

    public void setSql_operands(sql_Operands sql_operands) {
        this.sql_operands = sql_operands;
    }

}