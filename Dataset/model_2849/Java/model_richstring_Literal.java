





import java.util.List;
import java.util.ArrayList;

public class model_richstring_Literal extends LinePart {

    private int length;
    private int offset;



    public model_richstring_Literal(
        int length,        int offset    ) {
        super(
        );
        this.length = length;
        this.offset = offset;
    }


    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public int getOffset() {
        return offset;
    }

    public void setOffset(int offset) {
        this.offset = offset;
    }


}