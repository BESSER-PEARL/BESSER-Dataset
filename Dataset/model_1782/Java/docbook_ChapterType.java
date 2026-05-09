





import java.util.List;
import java.util.ArrayList;

public class docbook_ChapterType  {

    private String mixed;
    private String title;
    private String para;





    private docbook_BookType docbook_booktype;


    public docbook_ChapterType(
        String mixed,        String title,        String para    ) {
        this.mixed = mixed;
        this.title = title;
        this.para = para;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getPara() {
        return para;
    }

    public void setPara(String para) {
        this.para = para;
    }

    public docbook_BookType getDocbook_booktype() {
        return docbook_booktype;
    }

    public void setDocbook_booktype(docbook_BookType docbook_booktype) {
        this.docbook_booktype = docbook_booktype;
    }

}