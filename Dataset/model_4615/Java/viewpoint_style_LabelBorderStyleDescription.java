





import java.util.List;
import java.util.ArrayList;

public class viewpoint_style_LabelBorderStyleDescription  {

    private int cornerWidth;
    private int cornerHeight;
    private String id;
    private String name;



    public viewpoint_style_LabelBorderStyleDescription(
        int cornerWidth,        int cornerHeight,        String id,        String name    ) {
        this.cornerWidth = cornerWidth;
        this.cornerHeight = cornerHeight;
        this.id = id;
        this.name = name;
    }


    public int getCornerwidth() {
        return cornerWidth;
    }

    public void setCornerwidth(int cornerWidth) {
        this.cornerWidth = cornerWidth;
    }
    public int getCornerheight() {
        return cornerHeight;
    }

    public void setCornerheight(int cornerHeight) {
        this.cornerHeight = cornerHeight;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}