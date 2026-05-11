





import java.util.List;
import java.util.ArrayList;

public class model_Arc extends Shape {

    private int start;
    private int length;



    public model_Arc(
        int start,        int length    ) {
        super(
        );
        this.start = start;
        this.length = length;
    }


    public int getStart() {
        return start;
    }

    public void setStart(int start) {
        this.start = start;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }


}