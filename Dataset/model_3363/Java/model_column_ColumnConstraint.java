





import java.util.List;
import java.util.ArrayList;

public class model_column_ColumnConstraint  {

    private String name;





    private Column column;


    public model_column_ColumnConstraint(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Column getColumn() {
        return column;
    }

    public void setColumn(Column column) {
        this.column = column;
    }

}