





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_Rectangle2D  {

    private float height;
    private float x;
    private float width;
    private float y;





    private gmfgraph_SVGFigure gmfgraph_svgfigure;


    public gmfgraph_Rectangle2D(
        float height,        float x,        float width,        float y    ) {
        this.height = height;
        this.x = x;
        this.width = width;
        this.y = y;
    }


    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }

    public gmfgraph_SVGFigure getGmfgraph_svgfigure() {
        return gmfgraph_svgfigure;
    }

    public void setGmfgraph_svgfigure(gmfgraph_SVGFigure gmfgraph_svgfigure) {
        this.gmfgraph_svgfigure = gmfgraph_svgfigure;
    }

}