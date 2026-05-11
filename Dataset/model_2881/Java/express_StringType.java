





import java.util.List;
import java.util.ArrayList;

public class express_StringType extends BuiltInType {

    private boolean fixed;
    private int size;



    public express_StringType(
        boolean fixed,        int size    ) {
        super(
        );
        this.fixed = fixed;
        this.size = size;
    }


    public boolean getFixed() {
        return fixed;
    }

    public void setFixed(boolean fixed) {
        this.fixed = fixed;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }


}