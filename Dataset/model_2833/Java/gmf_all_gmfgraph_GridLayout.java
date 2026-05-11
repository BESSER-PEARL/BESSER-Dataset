





import java.util.List;
import java.util.ArrayList;

public class gmf_all_gmfgraph_GridLayout extends Layout {

    private int numColumns;
    private boolean equalWidth;



    public gmf_all_gmfgraph_GridLayout(
        int numColumns,        boolean equalWidth    ) {
        super(
        );
        this.numColumns = numColumns;
        this.equalWidth = equalWidth;
    }


    public int getNumcolumns() {
        return numColumns;
    }

    public void setNumcolumns(int numColumns) {
        this.numColumns = numColumns;
    }
    public boolean getEqualwidth() {
        return equalWidth;
    }

    public void setEqualwidth(boolean equalWidth) {
        this.equalWidth = equalWidth;
    }


}