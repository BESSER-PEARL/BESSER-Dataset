





import java.util.List;
import java.util.ArrayList;

public class tExp_Size extends Constraint {

    private int minSize;
    private int maxSize;



    public tExp_Size(
        int minSize,        int maxSize    ) {
        super(
        );
        this.minSize = minSize;
        this.maxSize = maxSize;
    }


    public int getMinsize() {
        return minSize;
    }

    public void setMinsize(int minSize) {
        this.minSize = minSize;
    }
    public int getMaxsize() {
        return maxSize;
    }

    public void setMaxsize(int maxSize) {
        this.maxSize = maxSize;
    }


}