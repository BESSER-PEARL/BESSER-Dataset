





import java.util.List;
import java.util.ArrayList;

public class flowgraph_Item  {

    private String txt;
    private int line;



    public flowgraph_Item(
        String txt,        int line    ) {
        this.txt = txt;
        this.line = line;
    }


    public String getTxt() {
        return txt;
    }

    public void setTxt(String txt) {
        this.txt = txt;
    }
    public int getLine() {
        return line;
    }

    public void setLine(int line) {
        this.line = line;
    }


}