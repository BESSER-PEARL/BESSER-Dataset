





import java.util.List;
import java.util.ArrayList;

public class mm_algorithms_RoundedRectangle extends GraphicsAlgorithm {

    private int cornerWidth;
    private int cornerHeight;



    public mm_algorithms_RoundedRectangle(
        int cornerWidth,        int cornerHeight    ) {
        super(
        );
        this.cornerWidth = cornerWidth;
        this.cornerHeight = cornerHeight;
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


}