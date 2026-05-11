





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_BasicFont extends Font {

    private String style;
    private String faceName;
    private int height;



    public gmfgraph_BasicFont(
        String style,        String faceName,        int height    ) {
        super(
        );
        this.style = style;
        this.faceName = faceName;
        this.height = height;
    }


    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getFacename() {
        return faceName;
    }

    public void setFacename(String faceName) {
        this.faceName = faceName;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }


}