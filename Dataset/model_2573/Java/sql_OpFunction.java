





import java.util.List;
import java.util.ArrayList;

public class sql_OpFunction  {

    private String fname;





    private sql_GroupByColumnFull sql_groupbycolumnfull;


    public sql_OpFunction(
        String fname    ) {
        this.fname = fname;
    }


    public String getFname() {
        return fname;
    }

    public void setFname(String fname) {
        this.fname = fname;
    }

    public sql_GroupByColumnFull getSql_groupbycolumnfull() {
        return sql_groupbycolumnfull;
    }

    public void setSql_groupbycolumnfull(sql_GroupByColumnFull sql_groupbycolumnfull) {
        this.sql_groupbycolumnfull = sql_groupbycolumnfull;
    }

}