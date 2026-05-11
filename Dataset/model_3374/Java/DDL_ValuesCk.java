





import java.util.List;
import java.util.ArrayList;

public class DDL_ValuesCk  {

    private String logConjuntion;
    private String comparator;
    private String columnName;
    private String value;





    private DDL_Ck ddl_ck;


    public DDL_ValuesCk(
        String logConjuntion,        String comparator,        String columnName,        String value    ) {
        this.logConjuntion = logConjuntion;
        this.comparator = comparator;
        this.columnName = columnName;
        this.value = value;
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
    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public DDL_Ck getDdl_ck() {
        return ddl_ck;
    }

    public void setDdl_ck(DDL_Ck ddl_ck) {
        this.ddl_ck = ddl_ck;
    }

}