





import java.util.List;
import java.util.ArrayList;

public class Docbook_ChapterType  {

    private String annotations;





    private Docbook_TitleType docbook_titletype;




    private Docbook_BookType docbook_booktype;




    private List<Docbook_ParaType> docbook_paratypes;


    public Docbook_ChapterType(
        String annotations    ) {
        this.annotations = annotations;
        this.docbook_paratypes = new ArrayList<>();
    }

    public Docbook_ChapterType(
        String annotations        ArrayList<Docbook_ParaType> docbook_paratypes    ) {
        this.annotations = annotations;
        this.docbook_paratypes = docbook_paratypes;
    }

    public String getAnnotations() {
        return annotations;
    }

    public void setAnnotations(String annotations) {
        this.annotations = annotations;
    }

    public Docbook_TitleType getDocbook_titletype() {
        return docbook_titletype;
    }

    public void setDocbook_titletype(Docbook_TitleType docbook_titletype) {
        this.docbook_titletype = docbook_titletype;
    }
    public Docbook_BookType getDocbook_booktype() {
        return docbook_booktype;
    }

    public void setDocbook_booktype(Docbook_BookType docbook_booktype) {
        this.docbook_booktype = docbook_booktype;
    }
    public List<Docbook_ParaType> getDocbook_paratypes() {
        return docbook_paratypes;
    }

    public void addDocbook_paratype(Docbook_paratype docbook_paratype) {
        this.docbook_paratypes.add(docbook_paratype);
    }

}