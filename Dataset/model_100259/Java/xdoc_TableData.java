





import java.util.List;
import java.util.ArrayList;

public class xdoc_TableData  {






    private List<xdoc_TextOrMarkup> xdoc_textormarkups;




    private xdoc_TableRow xdoc_tablerow;


    public xdoc_TableData(
    ) {
        this.xdoc_textormarkups = new ArrayList<>();
    }

    public xdoc_TableData(
        ArrayList<xdoc_TextOrMarkup> xdoc_textormarkups    ) {
        this.xdoc_textormarkups = xdoc_textormarkups;
    }


    public List<xdoc_TextOrMarkup> getXdoc_textormarkups() {
        return xdoc_textormarkups;
    }

    public void addXdoc_textormarkup(Xdoc_textormarkup xdoc_textormarkup) {
        this.xdoc_textormarkups.add(xdoc_textormarkup);
    }
    public xdoc_TableRow getXdoc_tablerow() {
        return xdoc_tablerow;
    }

    public void setXdoc_tablerow(xdoc_TableRow xdoc_tablerow) {
        this.xdoc_tablerow = xdoc_tablerow;
    }

}