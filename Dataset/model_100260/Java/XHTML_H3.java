





import java.util.List;
import java.util.ArrayList;

public class XHTML_H3 extends Attrs, Heading {






    private List<Inline> inlines;


    public XHTML_H3(
    ) {
        super(
        );
        this.inlines = new ArrayList<>();
    }

    public XHTML_H3(
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