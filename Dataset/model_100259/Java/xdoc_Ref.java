





import java.util.List;
import java.util.ArrayList;

public class xdoc_Ref extends MarkupInCode, MarkUp {






    private List<xdoc_TextOrMarkup> xdoc_textormarkups;




    private xdoc_Identifiable xdoc_identifiable;


    public xdoc_Ref(
    ) {
        super(
        );
        this.xdoc_textormarkups = new ArrayList<>();
    }

    public xdoc_Ref(
        ArrayList<xdoc_TextOrMarkup> xdoc_textormarkups    ) {
        this.xdoc_textormarkups = xdoc_textormarkups;
    }


    public List<xdoc_TextOrMarkup> getXdoc_textormarkups() {
        return xdoc_textormarkups;
    }

    public void addXdoc_textormarkup(Xdoc_textormarkup xdoc_textormarkup) {
        this.xdoc_textormarkups.add(xdoc_textormarkup);
    }
    public xdoc_Identifiable getXdoc_identifiable() {
        return xdoc_identifiable;
    }

    public void setXdoc_identifiable(xdoc_Identifiable xdoc_identifiable) {
        this.xdoc_identifiable = xdoc_identifiable;
    }

}