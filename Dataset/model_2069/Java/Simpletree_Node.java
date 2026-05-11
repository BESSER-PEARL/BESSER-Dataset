





import java.util.List;
import java.util.ArrayList;

public class Simpletree_Node extends Text {

    private int stopLineIndex;
    private int stopIndex;
    private int startIndex;
    private int startLineIndex;



    public Simpletree_Node(
        int stopLineIndex,        int stopIndex,        int startIndex,        int startLineIndex    ) {
        super(
        );
        this.stopLineIndex = stopLineIndex;
        this.stopIndex = stopIndex;
        this.startIndex = startIndex;
        this.startLineIndex = startLineIndex;
    }


    public int getStoplineindex() {
        return stopLineIndex;
    }

    public void setStoplineindex(int stopLineIndex) {
        this.stopLineIndex = stopLineIndex;
    }
    public int getStopindex() {
        return stopIndex;
    }

    public void setStopindex(int stopIndex) {
        this.stopIndex = stopIndex;
    }
    public int getStartindex() {
        return startIndex;
    }

    public void setStartindex(int startIndex) {
        this.startIndex = startIndex;
    }
    public int getStartlineindex() {
        return startLineIndex;
    }

    public void setStartlineindex(int startLineIndex) {
        this.startLineIndex = startLineIndex;
    }


}