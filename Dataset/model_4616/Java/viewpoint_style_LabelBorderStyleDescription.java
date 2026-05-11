





import java.util.List;
import java.util.ArrayList;

public class viewpoint_style_LabelBorderStyleDescription  {

    private String id;
    private int cornerWidth;
    private int cornerHeight;
    private String name;



    public viewpoint_style_LabelBorderStyleDescription(
        String id,        int cornerWidth,        int cornerHeight,        String name    ) {
        this.id = id;
        this.cornerWidth = cornerWidth;
        this.cornerHeight = cornerHeight;
        this.name = name;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}