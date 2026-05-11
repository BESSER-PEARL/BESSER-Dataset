





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Insets  {

    private int bottom;
    private int left;
    private int top;
    private int right;





    private gmfgraph_Figure gmfgraph_figure;


    public gmfgraph_Insets(
        int bottom,        int left,        int top,        int right    ) {
        this.bottom = bottom;
        this.left = left;
        this.top = top;
        this.right = right;
    }


    public int getBottom() {
        return bottom;
    }

    public void setBottom(int bottom) {
        this.bottom = bottom;
    }
    public int getLeft() {
        return left;
    }

    public void setLeft(int left) {
        this.left = left;
    }
    public int getTop() {
        return top;
    }

    public void setTop(int top) {
        this.top = top;
    }
    public int getRight() {
        return right;
    }

    public void setRight(int right) {
        this.right = right;
    }

    public gmfgraph_Figure getGmfgraph_figure() {
        return gmfgraph_figure;
    }

    public void setGmfgraph_figure(gmfgraph_Figure gmfgraph_figure) {
        this.gmfgraph_figure = gmfgraph_figure;
    }

}