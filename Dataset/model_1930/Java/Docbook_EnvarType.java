





import java.util.List;
import java.util.ArrayList;

public class Docbook_EnvarType  {

    private String mixed;





    private List<Docbook_ReplaceableType> docbook_replaceabletypes;


    public Docbook_EnvarType(
        String mixed    ) {
        this.mixed = mixed;
        this.docbook_replaceabletypes = new ArrayList<>();
    }

    public Docbook_EnvarType(
        String mixed        ArrayList<Docbook_ReplaceableType> docbook_replaceabletypes    ) {
        this.mixed = mixed;
        this.docbook_replaceabletypes = docbook_replaceabletypes;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<Docbook_ReplaceableType> getDocbook_replaceabletypes() {
        return docbook_replaceabletypes;
    }

    public void addDocbook_replaceabletype(Docbook_replaceabletype docbook_replaceabletype) {
        this.docbook_replaceabletypes.add(docbook_replaceabletype);
    }

}