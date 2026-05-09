





import java.util.List;
import java.util.ArrayList;

public class emig_LocatedElement  {

    private int offset;
    private int endoffset;
    private int line;
    private int endline;



    public emig_LocatedElement(
        int offset,        int endoffset,        int line,        int endline    ) {
        this.offset = offset;
        this.endoffset = endoffset;
        this.line = line;
        this.endline = endline;
    }


    public int getOffset() {
        return offset;
    }

    public void setOffset(int offset) {
        this.offset = offset;
    }
    public int getEndoffset() {
        return endoffset;
    }

    public void setEndoffset(int endoffset) {
        this.endoffset = endoffset;
    }
    public int getLine() {
        return line;
    }

    public void setLine(int line) {
        this.line = line;
    }
    public int getEndline() {
        return endline;
    }

    public void setEndline(int endline) {
        this.endline = endline;
    }


}