





import java.util.List;
import java.util.ArrayList;

public class gast_core_Root extends ModelElement {

    private int linesOfCode;
    private int linesOfComments;



    public gast_core_Root(
        int linesOfCode,        int linesOfComments    ) {
        super(
        );
        this.linesOfCode = linesOfCode;
        this.linesOfComments = linesOfComments;
    }


    public int getLinesofcode() {
        return linesOfCode;
    }

    public void setLinesofcode(int linesOfCode) {
        this.linesOfCode = linesOfCode;
    }
    public int getLinesofcomments() {
        return linesOfComments;
    }

    public void setLinesofcomments(int linesOfComments) {
        this.linesOfComments = linesOfComments;
    }


}