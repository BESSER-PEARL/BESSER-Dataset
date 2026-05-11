





import java.util.List;
import java.util.ArrayList;

public class viewpoint_style_LabelBorderStyleDescription  {

    private int cornerHeight;
    private String name;
    private String id;
    private int cornerWidth;



    public viewpoint_style_LabelBorderStyleDescription(
        int cornerHeight,        String name,        String id,        int cornerWidth    ) {
        this.cornerHeight = cornerHeight;
        this.name = name;
        this.id = id;
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


}