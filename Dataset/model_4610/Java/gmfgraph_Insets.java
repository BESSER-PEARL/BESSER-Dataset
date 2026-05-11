





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Insets  {

    private int top;
    private int left;
    private int right;
    private int bottom;





    private gmfgraph_MarginBorder gmfgraph_marginborder;


    public gmfgraph_Insets(
        int top,        int left,        int right,        int bottom    ) {
        this.top = top;
        this.left = left;
        this.right = right;
        this.bottom = bottom;
    }


    public int getTop() {
        return top;
    }

    public void setTop(int top) {
        this.top = top;
    }
    public int getLeft() {
        return left;
    }

    public void setLeft(int left) {
        this.left = left;
    }
    public int getRight() {
        return right;
    }

    public void setRight(int right) {
        this.right = right;
    }
    public int getBottom() {
        return bottom;
    }

    public void setBottom(int bottom) {
        this.bottom = bottom;
    }

    public gmfgraph_MarginBorder getGmfgraph_marginborder() {
        return gmfgraph_marginborder;
    }

    public void setGmfgraph_marginborder(gmfgraph_MarginBorder gmfgraph_marginborder) {
        this.gmfgraph_marginborder = gmfgraph_marginborder;
    }

}