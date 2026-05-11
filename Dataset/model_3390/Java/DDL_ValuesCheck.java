





import java.util.List;
import java.util.ArrayList;

public class DDL_ValuesCheck  {

    private String columnName;
    private String logConjuntion;
    private String comparator;
    private String value;





    private DDL_Check ddl_check;


    public DDL_ValuesCheck(
        String columnName,        String logConjuntion,        String comparator,        String value    ) {
        this.columnName = columnName;
        this.logConjuntion = logConjuntion;
        this.comparator = comparator;
        this.value = value;
    }


    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }
    public String getLogconjuntion() {
        return logConjuntion;
    }

    public void setLogconjuntion(String logConjuntion) {
        this.logConjuntion = logConjuntion;
    }
    public String getComparator() {
        return comparator;
    }

    public void setComparator(String comparator) {
        this.comparator = comparator;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public DDL_Check getDdl_check() {
        return ddl_check;
    }

    public void setDdl_check(DDL_Check ddl_check) {
        this.ddl_check = ddl_check;
    }

}