





import java.util.List;
import java.util.ArrayList;

public class model_R4ETextPosition extends R4EPosition {

    private int startLine;
    private int startPosition;
    private int endLine;
    private int length;



    public model_R4ETextPosition(
        int startLine,        int startPosition,        int endLine,        int length    ) {
        super(
        );
        this.startLine = startLine;
        this.startPosition = startPosition;
        this.endLine = endLine;
        this.length = length;
    }


    public int getStartline() {
        return startLine;
    }

    public void setStartline(int startLine) {
        this.startLine = startLine;
    }
    public int getStartposition() {
        return startPosition;
    }

    public void setStartposition(int startPosition) {
        this.startPosition = startPosition;
    }
    public int getEndline() {
        return endLine;
    }

    public void setEndline(int endLine) {
        this.endLine = endLine;
    }
    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }


}