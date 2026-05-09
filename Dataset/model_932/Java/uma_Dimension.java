





import java.util.List;
import java.util.ArrayList;

public class uma_Dimension  {

    private String width;
    private String height;





    private uma_GraphNode uma_graphnode;


    public uma_Dimension(
        String width,        String height    ) {
        this.width = width;
        this.height = height;
    }


    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }

    public uma_GraphNode getUma_graphnode() {
        return uma_graphnode;
    }

    public void setUma_graphnode(uma_GraphNode uma_graphnode) {
        this.uma_graphnode = uma_graphnode;
    }

}