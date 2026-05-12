





import java.util.List;
import java.util.ArrayList;

public class XHTML_Caption extends Attrs {






    private List<Inline> inlines;


    public XHTML_Caption(
    ) {
        super(
        );
        this.inlines = new ArrayList<>();
    }

    public XHTML_Caption(
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