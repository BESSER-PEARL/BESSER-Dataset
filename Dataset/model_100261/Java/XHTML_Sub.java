





import java.util.List;
import java.util.ArrayList;

public class XHTML_Sub extends Attrs, Phrase {






    private List<Inline> inlines;


    public XHTML_Sub(
    ) {
        super(
        );
        this.inlines = new ArrayList<>();
    }

    public XHTML_Sub(
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