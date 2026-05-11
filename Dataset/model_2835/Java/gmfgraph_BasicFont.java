





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_BasicFont extends Font {

    private int height;
    private String faceName;
    private String style;



    public gmfgraph_BasicFont(
        int height,        String faceName,        String style    ) {
        super(
        );
        this.height = height;
        this.faceName = faceName;
        this.style = style;
    }


    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public String getFacename() {
        return faceName;
    }

    public void setFacename(String faceName) {
        this.faceName = faceName;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }


}