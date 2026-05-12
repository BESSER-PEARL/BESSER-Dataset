





import java.util.List;
import java.util.ArrayList;

public class sql_Offset  {

    private int offset;





    private sql_Select sql_select;


    public sql_Offset(
        int offset    ) {
        this.offset = offset;
    }


    public int getOffset() {
        return offset;
    }

    public void setOffset(int offset) {
        this.offset = offset;
    }

    public sql_Select getSql_select() {
        return sql_select;
    }

    public void setSql_select(sql_Select sql_select) {
        this.sql_select = sql_select;
    }

}