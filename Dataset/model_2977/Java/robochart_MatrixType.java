





import java.util.List;
import java.util.ArrayList;

public class robochart_MatrixType extends Type {

    private int rows;
    private int columns;



    public robochart_MatrixType(
        int rows,        int columns    ) {
        super(
        );
        this.rows = rows;
        this.columns = columns;
    }


    public int getRows() {
        return rows;
    }

    public void setRows(int rows) {
        this.rows = rows;
    }
    public int getColumns() {
        return columns;
    }

    public void setColumns(int columns) {
        this.columns = columns;
    }


}