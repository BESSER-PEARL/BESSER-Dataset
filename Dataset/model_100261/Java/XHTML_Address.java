





import java.util.List;
import java.util.ArrayList;

public class XHTML_Address extends Attrs, Blocktext {






    private List<Inline> inlines;


    public XHTML_Address(
    ) {
        super(
        );
        this.inlines = new ArrayList<>();
    }

    public XHTML_Address(
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