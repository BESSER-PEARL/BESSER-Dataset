





import java.util.List;
import java.util.ArrayList;

public class sql_Limit  {

    private int l1;





    private sql_Select sql_select;




    private sql_IntegerValue sql_integervalue;


    public sql_Limit(
        int l1    ) {
        this.l1 = l1;
    }


    public int getL1() {
        return l1;
    }

    public void setL1(int l1) {
        this.l1 = l1;
    }

    public sql_Select getSql_select() {
        return sql_select;
    }

    public void setSql_select(sql_Select sql_select) {
        this.sql_select = sql_select;
    }
    public sql_IntegerValue getSql_integervalue() {
        return sql_integervalue;
    }

    public void setSql_integervalue(sql_IntegerValue sql_integervalue) {
        this.sql_integervalue = sql_integervalue;
    }

}