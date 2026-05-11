





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Dimension  {

    private int dx;
    private int dy;





    private gmfgraph_DefaultSizeFacet gmfgraph_defaultsizefacet;


    public gmfgraph_Dimension(
        int dx,        int dy    ) {
        this.dx = dx;
        this.dy = dy;
    }


    public int getDx() {
        return dx;
    }

    public void setDx(int dx) {
        this.dx = dx;
    }
    public int getDy() {
        return dy;
    }

    public void setDy(int dy) {
        this.dy = dy;
    }

    public gmfgraph_DefaultSizeFacet getGmfgraph_defaultsizefacet() {
        return gmfgraph_defaultsizefacet;
    }

    public void setGmfgraph_defaultsizefacet(gmfgraph_DefaultSizeFacet gmfgraph_defaultsizefacet) {
        this.gmfgraph_defaultsizefacet = gmfgraph_defaultsizefacet;
    }

}