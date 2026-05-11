





import java.util.List;
import java.util.ArrayList;

public class viewpoint_style_LabelBorderStyleDescription  {

    private int cornerHeight;
    private int cornerWidth;
    private String name;
    private String id;



    public viewpoint_style_LabelBorderStyleDescription(
        int cornerHeight,        int cornerWidth,        String name,        String id    ) {
        this.cornerHeight = cornerHeight;
        this.cornerWidth = cornerWidth;
        this.name = name;
        this.id = id;
    }


    public int getCornerheight() {
        return cornerHeight;
    }

    public void setCornerheight(int cornerHeight) {
        this.cornerHeight = cornerHeight;
    }
    public int getCornerwidth() {
        return cornerWidth;
    }

    public void setCornerwidth(int cornerWidth) {
        this.cornerWidth = cornerWidth;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}