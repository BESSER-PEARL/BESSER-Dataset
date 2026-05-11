





import java.util.List;
import java.util.ArrayList;

public class gmf_all_gmfgraph_RoundedRectangle extends Shape {

    private int cornerHeight;
    private int cornerWidth;



    public gmf_all_gmfgraph_RoundedRectangle(
        int cornerHeight,        int cornerWidth    ) {
        super(
        );
        this.cornerHeight = cornerHeight;
        this.cornerWidth = cornerWidth;
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


}