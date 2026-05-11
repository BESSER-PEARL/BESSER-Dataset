





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_Arc extends Shape {

    private int length;
    private int start;



    public VisualInterface_Arc(
        int length,        int start    ) {
        super(
        );
        this.length = length;
        this.start = start;
    }


    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }
    public int getStart() {
        return start;
    }

    public void setStart(int start) {
        this.start = start;
    }


}