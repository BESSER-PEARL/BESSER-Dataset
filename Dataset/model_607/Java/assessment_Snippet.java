





import java.util.List;
import java.util.ArrayList;

public class assessment_Snippet extends Contents, GraphNode {

    private int lineEnd;
    private int lineStart;
    private int columnStart;
    private int columnEnd;



    public assessment_Snippet(
        int lineEnd,        int lineStart,        int columnStart,        int columnEnd    ) {
        super(
        );
        this.lineEnd = lineEnd;
        this.lineStart = lineStart;
        this.columnStart = columnStart;
        this.columnEnd = columnEnd;
    }


    public int getLineend() {
        return lineEnd;
    }

    public void setLineend(int lineEnd) {
        this.lineEnd = lineEnd;
    }
    public int getLinestart() {
        return lineStart;
    }

    public void setLinestart(int lineStart) {
        this.lineStart = lineStart;
    }
    public int getColumnstart() {
        return columnStart;
    }

    public void setColumnstart(int columnStart) {
        this.columnStart = columnStart;
    }
    public int getColumnend() {
        return columnEnd;
    }

    public void setColumnend(int columnEnd) {
        this.columnEnd = columnEnd;
    }


}