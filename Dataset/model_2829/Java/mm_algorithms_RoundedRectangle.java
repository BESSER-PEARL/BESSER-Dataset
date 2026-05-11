





import java.util.List;
import java.util.ArrayList;

public class mm_algorithms_RoundedRectangle extends GraphicsAlgorithm {

    private int cornerHeight;
    private int cornerWidth;



    public mm_algorithms_RoundedRectangle(
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