





import java.util.List;
import java.util.ArrayList;

public class gmf_all_gmfgraph_BasicFont extends Font {

    private String faceName;
    private int height;
    private String style;



    public gmf_all_gmfgraph_BasicFont(
        String faceName,        int height,        String style    ) {
        super(
        );
        this.faceName = faceName;
        this.height = height;
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
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }


}