





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_LineBorder extends Border {

    private int width;





    private gmfgraph_Color gmfgraph_color;


    public gmfgraph_LineBorder(
        int width    ) {
        super(
        );
        this.width = width;
    }


    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }

    public gmfgraph_Color getGmfgraph_color() {
        return gmfgraph_color;
    }

    public void setGmfgraph_color(gmfgraph_Color gmfgraph_color) {
        this.gmfgraph_color = gmfgraph_color;
    }

}