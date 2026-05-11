





import java.util.List;
import java.util.ArrayList;

public class fxg_ColorMatrixFilter extends Filter {

    private String matrix;



    public fxg_ColorMatrixFilter(
        String matrix    ) {
        super(
        );
        this.matrix = matrix;
    }


    public String getMatrix() {
        return matrix;
    }

    public void setMatrix(String matrix) {
        this.matrix = matrix;
    }


}