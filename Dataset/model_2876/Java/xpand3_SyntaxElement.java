





import java.util.List;
import java.util.ArrayList;

public class xpand3_SyntaxElement  {

    private int start;
    private String fileName;
    private int line;
    private int end;



    public xpand3_SyntaxElement(
        int start,        String fileName,        int line,        int end    ) {
        this.start = start;
        this.fileName = fileName;
        this.line = line;
        this.end = end;
    }


    public int getStart() {
        return start;
    }

    public void setStart(int start) {
        this.start = start;
    }
    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }
    public int getLine() {
        return line;
    }

    public void setLine(int line) {
        this.line = line;
    }
    public int getEnd() {
        return end;
    }

    public void setEnd(int end) {
        this.end = end;
    }


}