





import java.util.List;
import java.util.ArrayList;

public class errors_ColumnCk  {

    private String columnName;





    private errors_CheckError errors_checkerror;


    public errors_ColumnCk(
        String columnName    ) {
        this.columnName = columnName;
    }


    public String getColumnname() {
        return columnName;
    }

    public void setColumnname(String columnName) {
        this.columnName = columnName;
    }

    public errors_CheckError getErrors_checkerror() {
        return errors_checkerror;
    }

    public void setErrors_checkerror(errors_CheckError errors_checkerror) {
        this.errors_checkerror = errors_checkerror;
    }

}