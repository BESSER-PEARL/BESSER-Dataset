





import java.util.List;
import java.util.ArrayList;

public class systemmodel_MatrixType extends DataType {

    private String columns;
    private String rows;



    public systemmodel_MatrixType(
        String columns,        String rows    ) {
        super(
        );
        this.columns = columns;
        this.rows = rows;
    }


    public String getColumns() {
        return columns;
    }

    public void setColumns(String columns) {
        this.columns = columns;
    }
    public String getRows() {
        return rows;
    }

    public void setRows(String rows) {
        this.rows = rows;
    }


}