





import java.util.List;
import java.util.ArrayList;

public class XHTML_Span extends Attrs, Specialpre {






    private List<Inline> inlines;


    public XHTML_Span(
    ) {
        super(
        );
        this.inlines = new ArrayList<>();
    }

    public XHTML_Span(
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