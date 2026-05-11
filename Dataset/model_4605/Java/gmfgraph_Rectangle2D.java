





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Rectangle2D  {

    private float x;
    private float y;
    private float height;
    private float width;





    private gmfgraph_SVGFigure gmfgraph_svgfigure;


    public gmfgraph_Rectangle2D(
        float x,        float y,        float height,        float width    ) {
        this.x = x;
        this.y = y;
        this.height = height;
        this.width = width;
    }


    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }

    public gmfgraph_SVGFigure getGmfgraph_svgfigure() {
        return gmfgraph_svgfigure;
    }

    public void setGmfgraph_svgfigure(gmfgraph_SVGFigure gmfgraph_svgfigure) {
        this.gmfgraph_svgfigure = gmfgraph_svgfigure;
    }

}