





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_GridLayout extends Layout {

    private boolean equalWidth;
    private int numColumns;





    private gmfgraph_Dimension gmfgraph_dimension;




    private gmfgraph_Dimension gmfgraph_dimension;


    public gmfgraph_GridLayout(
        boolean equalWidth,        int numColumns    ) {
        super(
        );
        this.equalWidth = equalWidth;
        this.numColumns = numColumns;
    }


    public boolean getEqualwidth() {
        return equalWidth;
    }

    public void setEqualwidth(boolean equalWidth) {
        this.equalWidth = equalWidth;
    }
    public int getNumcolumns() {
        return numColumns;
    }

    public void setNumcolumns(int numColumns) {
        this.numColumns = numColumns;
    }

    public gmfgraph_Dimension getGmfgraph_dimension() {
        return gmfgraph_dimension;
    }

    public void setGmfgraph_dimension(gmfgraph_Dimension gmfgraph_dimension) {
        this.gmfgraph_dimension = gmfgraph_dimension;
    }
    public gmfgraph_Dimension getGmfgraph_dimension() {
        return gmfgraph_dimension;
    }

    public void setGmfgraph_dimension(gmfgraph_Dimension gmfgraph_dimension) {
        this.gmfgraph_dimension = gmfgraph_dimension;
    }

}