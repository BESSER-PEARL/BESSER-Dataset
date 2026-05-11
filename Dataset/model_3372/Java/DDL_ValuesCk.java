





import java.util.List;
import java.util.ArrayList;

public class DDL_ValuesCk  {

    private String value;
    private String comparator;
    private String logConjuntion;
    private String columnName;





    private DDL_Ck ddl_ck;


    public DDL_ValuesCk(
        String value,        String comparator,        String logConjuntion,        String columnName    ) {
        this.value = value;
        this.comparator = comparator;
        this.logConjuntion = logConjuntion;
        this.columnName = columnName;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getComparator() {
        return comparator;
    }

    public void setComparator(String comparator) {
        this.comparator = comparator;
    }
    public String getLogconjuntion() {
        return logConjuntion;
    }

    public void setLogconjuntion(String logConjuntion) {
        this.logConjuntion = logConjuntion;
    }
    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }

    public DDL_Ck getDdl_ck() {
        return ddl_ck;
    }

    public void setDdl_ck(DDL_Ck ddl_ck) {
        this.ddl_ck = ddl_ck;
    }

}