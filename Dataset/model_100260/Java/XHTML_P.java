





import java.util.List;
import java.util.ArrayList;

public class XHTML_P extends Attrs, block, ButtonContent {






    private List<Inline> inlines;


    public XHTML_P(
    ) {
        super(
        );
        this.inlines = new ArrayList<>();
    }

    public XHTML_P(
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