





import java.util.List;
import java.util.ArrayList;

public class XHTML_Q extends Attrs, Phrase {






    private List<Inline> inlines;




    private URI uri;


    public XHTML_Q(
    ) {
        super(
        );
        this.inlines = new ArrayList<>();
    }

    public XHTML_Q(
        ArrayList<Inline> inlines    ) {
        this.inlines = inlines;
    }


    public List<Inline> getInlines() {
        return inlines;
    }

    public void addInline(Inline inline) {
        this.inlines.add(inline);
    }
    public URI getUri() {
        return uri;
    }

    public void setUri(URI uri) {
        this.uri = uri;
    }

}