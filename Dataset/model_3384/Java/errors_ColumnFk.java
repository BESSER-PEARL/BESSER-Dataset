





import java.util.List;
import java.util.ArrayList;

public class errors_ColumnFk  {

    private String nameColumn;





    private errors_Table errors_table;


    public errors_ColumnFk(
        String nameColumn    ) {
        this.nameColumn = nameColumn;
    }


    public String getNamecolumn() {
        return nameColumn;
    }

    public void setNamecolumn(String nameColumn) {
        this.nameColumn = nameColumn;
    }

    public errors_Table getErrors_table() {
        return errors_table;
    }

    public void setErrors_table(errors_Table errors_table) {
        this.errors_table = errors_table;
    }

}