





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_GridLayout extends Layout {

    private int columns;



    public appBuilderDSL_GridLayout(
        int columns    ) {
        super(
        );
        this.columns = columns;
    }


    public int getColumns() {
        return columns;
    }

    public void setColumns(int columns) {
        this.columns = columns;
    }


}