





import java.util.List;
import java.util.ArrayList;

public class codemodel_MatrixType extends DataType {

    private String columns;
    private String rows;



    public codemodel_MatrixType(
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