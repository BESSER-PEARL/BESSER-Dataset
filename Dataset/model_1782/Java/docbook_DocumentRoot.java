





import java.util.List;
import java.util.ArrayList;

public class docbook_DocumentRoot  {

    private String mixed;
    private String para;
    private String title;
    private String info;





    private List<docbook_BookType> docbook_booktypes;




    private List<docbook_ChapterType> docbook_chaptertypes;


    public docbook_DocumentRoot(
        String mixed,        String para,        String title,        String info    ) {
        this.mixed = mixed;
        this.para = para;
        this.title = title;
        this.info = info;
        this.docbook_booktypes = new ArrayList<>();
        this.docbook_chaptertypes = new ArrayList<>();
    }

    public docbook_DocumentRoot(
        String mixed,        String para,        String title,        String info        ArrayList<docbook_BookType> docbook_booktypes,        ArrayList<docbook_ChapterType> docbook_chaptertypes    ) {
        this.mixed = mixed;
        this.para = para;
        this.title = title;
        this.info = info;
        this.docbook_booktypes = docbook_booktypes;
        this.docbook_chaptertypes = docbook_chaptertypes;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getPara() {
        return para;
    }

    public void setPara(String para) {
        this.para = para;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getInfo() {
        return info;
    }

    public void setInfo(String info) {
        this.info = info;
    }

    public List<docbook_BookType> getDocbook_booktypes() {
        return docbook_booktypes;
    }

    public void addDocbook_booktype(Docbook_booktype docbook_booktype) {
        this.docbook_booktypes.add(docbook_booktype);
    }
    public List<docbook_ChapterType> getDocbook_chaptertypes() {
        return docbook_chaptertypes;
    }

    public void addDocbook_chaptertype(Docbook_chaptertype docbook_chaptertype) {
        this.docbook_chaptertypes.add(docbook_chaptertype);
    }

}