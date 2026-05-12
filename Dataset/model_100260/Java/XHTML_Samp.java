





import java.util.List;
import java.util.ArrayList;

public class XHTML_Samp extends Attrs, Phrase {






    private List<Inline> inlines;


    public XHTML_Samp(
    ) {
        super(
        );
        this.inlines = new ArrayList<>();
    }

    public XHTML_Samp(
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