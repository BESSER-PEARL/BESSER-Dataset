





import java.util.List;
import java.util.ArrayList;

public class SQLDML_InExp extends Expression {

    private String columnName;



    public SQLDML_InExp(
        String columnName    ) {
        super(
        );
        this.columnName = columnName;
    }


    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }


}