





import java.util.List;
import java.util.ArrayList;

public class Documentation_InformalTableValue extends ParagraphValue {

    private int cols;



    public Documentation_InformalTableValue(
        int cols    ) {
        super(
        );
        this.cols = cols;
    }


    public int getCols() {
        return cols;
    }

    public void setCols(int cols) {
        this.cols = cols;
    }


}