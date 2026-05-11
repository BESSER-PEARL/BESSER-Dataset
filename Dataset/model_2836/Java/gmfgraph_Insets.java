





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Insets  {

    private int top;
    private int bottom;
    private int right;
    private int left;





    private gmfgraph_Figure gmfgraph_figure;


    public gmfgraph_Insets(
        int top,        int bottom,        int right,        int left    ) {
        this.top = top;
        this.bottom = bottom;
        this.right = right;
        this.left = left;
    }


    public int getTop() {
        return top;
    }

    public void setTop(int top) {
        this.top = top;
    }
    public int getBottom() {
        return bottom;
    }

    public void setBottom(int bottom) {
        this.bottom = bottom;
    }
    public int getRight() {
        return right;
    }

    public void setRight(int right) {
        this.right = right;
    }
    public int getLeft() {
        return left;
    }

    public void setLeft(int left) {
        this.left = left;
    }

    public gmfgraph_Figure getGmfgraph_figure() {
        return gmfgraph_figure;
    }

    public void setGmfgraph_figure(gmfgraph_Figure gmfgraph_figure) {
        this.gmfgraph_figure = gmfgraph_figure;
    }

}