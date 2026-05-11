





import java.util.List;
import java.util.ArrayList;

public class DML_DDL_ValuesCk  {

    private String comparator;
    private String value;
    private String logConjuntion;
    private String columnName;





    private DML_DDL_Ck dml_ddl_ck;


    public DML_DDL_ValuesCk(
        String comparator,        String value,        String logConjuntion,        String columnName    ) {
        this.comparator = comparator;
        this.value = value;
        this.logConjuntion = logConjuntion;
        this.columnName = columnName;
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

    public DML_DDL_Ck getDml_ddl_ck() {
        return dml_ddl_ck;
    }

    public void setDml_ddl_ck(DML_DDL_Ck dml_ddl_ck) {
        this.dml_ddl_ck = dml_ddl_ck;
    }

}