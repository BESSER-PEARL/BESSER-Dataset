





import java.util.List;
import java.util.ArrayList;

public class XHTML_Em extends Attrs, Phrase {






    private List<Inline> inlines;


    public XHTML_Em(
    ) {
        super(
        );
        this.inlines = new ArrayList<>();
    }

    public XHTML_Em(
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