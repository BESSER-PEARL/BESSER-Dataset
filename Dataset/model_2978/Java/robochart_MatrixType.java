





import java.util.List;
import java.util.ArrayList;

public class robochart_MatrixType extends Type {

    private int columns;
    private int rows;





    private robochart_Type robochart_type;


    public robochart_MatrixType(
        int columns,        int rows    ) {
        super(
        );
        this.columns = columns;
        this.rows = rows;
    }


    public int getColumns() {
        return columns;
    }

    public void setColumns(int columns) {
        this.columns = columns;
    }
    public int getRows() {
        return rows;
    }

    public void setRows(int rows) {
        this.rows = rows;
    }

    public robochart_Type getRobochart_type() {
        return robochart_type;
    }

    public void setRobochart_type(robochart_Type robochart_type) {
        this.robochart_type = robochart_type;
    }

}