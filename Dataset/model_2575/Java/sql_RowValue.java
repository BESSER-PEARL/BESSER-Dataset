





import java.util.List;
import java.util.ArrayList;

public class sql_RowValue extends RowValues {

    private String null;





    private sql_RowValues sql_rowvalues;


    public sql_RowValue(
        String null    ) {
        super(
        );
        this.null = null;
    }


    public String getNull() {
        return null;
    }

    public void setNull(String null) {
        this.null = null;
    }

    public sql_RowValues getSql_rowvalues() {
        return sql_rowvalues;
    }

    public void setSql_rowvalues(sql_RowValues sql_rowvalues) {
        this.sql_rowvalues = sql_rowvalues;
    }

}