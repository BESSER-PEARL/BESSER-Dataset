





import java.util.List;
import java.util.ArrayList;

public class XHTML_Dt extends DlElement {






    private List<Inline> inlines;


    public XHTML_Dt(
    ) {
        super(
        );
        this.inlines = new ArrayList<>();
    }

    public XHTML_Dt(
        ArrayList<Inline> inlines    ) {
        this.inlines = inlines;
    }


    public List<Inline> getInlines() {
        return inlines;
    }

    public void addInline(Inline inline) {
        this.inlines.add(inline);
    }

}