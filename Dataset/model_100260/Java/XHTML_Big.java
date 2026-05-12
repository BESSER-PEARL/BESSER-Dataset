





import java.util.List;
import java.util.ArrayList;

public class XHTML_Big extends Attrs, Fontstyle {






    private List<Inline> inlines;


    public XHTML_Big(
    ) {
        super(
        );
        this.inlines = new ArrayList<>();
    }

    public XHTML_Big(
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