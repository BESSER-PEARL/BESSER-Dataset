





import java.util.List;
import java.util.ArrayList;

public class sqlDSL_SInlinedSQLType  {

    private int value;





    private sqlDSL_SColumn sqldsl_scolumn;


    public sqlDSL_SInlinedSQLType(
        int value    ) {
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public sqlDSL_SColumn getSqldsl_scolumn() {
        return sqldsl_scolumn;
    }

    public void setSqldsl_scolumn(sqlDSL_SColumn sqldsl_scolumn) {
        this.sqldsl_scolumn = sqldsl_scolumn;
    }

}