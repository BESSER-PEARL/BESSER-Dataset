





import java.util.List;
import java.util.ArrayList;

public class xdoc_AbstractSection extends Identifiable {






    private List<xdoc_TextOrMarkup> xdoc_textormarkups;




    private xdoc_XdocFile xdoc_xdocfile;




    private xdoc_TextOrMarkup xdoc_textormarkup;


    public xdoc_AbstractSection(
    ) {
        super(
        );
        this.xdoc_textormarkups = new ArrayList<>();
    }

    public xdoc_AbstractSection(
        ArrayList<xdoc_TextOrMarkup> xdoc_textormarkups    ) {
        this.xdoc_textormarkups = xdoc_textormarkups;
    }


    public List<xdoc_TextOrMarkup> getXdoc_textormarkups() {
        return xdoc_textormarkups;
    }

    public void addXdoc_textormarkup(Xdoc_textormarkup xdoc_textormarkup) {
        this.xdoc_textormarkups.add(xdoc_textormarkup);
    }
    public xdoc_XdocFile getXdoc_xdocfile() {
        return xdoc_xdocfile;
    }

    public void setXdoc_xdocfile(xdoc_XdocFile xdoc_xdocfile) {
        this.xdoc_xdocfile = xdoc_xdocfile;
    }
    public xdoc_TextOrMarkup getXdoc_textormarkup() {
        return xdoc_textormarkup;
    }

    public void setXdoc_textormarkup(xdoc_TextOrMarkup xdoc_textormarkup) {
        this.xdoc_textormarkup = xdoc_textormarkup;
    }

}