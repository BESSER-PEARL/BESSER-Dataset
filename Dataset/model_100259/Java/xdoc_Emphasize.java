





import java.util.List;
import java.util.ArrayList;

public class xdoc_Emphasize extends MarkupInCode, MarkUp {






    private List<xdoc_TextOrMarkup> xdoc_textormarkups;


    public xdoc_Emphasize(
    ) {
        super(
        );
        this.xdoc_textormarkups = new ArrayList<>();
    }

    public xdoc_Emphasize(
        ArrayList<xdoc_TextOrMarkup> xdoc_textormarkups    ) {
        this.xdoc_textormarkups = xdoc_textormarkups;
    }


    public List<xdoc_TextOrMarkup> getXdoc_textormarkups() {
        return xdoc_textormarkups;
    }

    public void addXdoc_textormarkup(Xdoc_textormarkup xdoc_textormarkup) {
        this.xdoc_textormarkups.add(xdoc_textormarkup);
    }

}