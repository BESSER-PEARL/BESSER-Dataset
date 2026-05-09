





import java.util.List;
import java.util.ArrayList;

public class docbook_Sect1Type  {

    private String title;
    private String mixed;
    private String para;





    private docbook_DocumentRoot docbook_documentroot;




    private docbook_ChapterType docbook_chaptertype;


    public docbook_Sect1Type(
        String title,        String mixed,        String para    ) {
        this.title = title;
        this.mixed = mixed;
        this.para = para;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
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

    public docbook_DocumentRoot getDocbook_documentroot() {
        return docbook_documentroot;
    }

    public void setDocbook_documentroot(docbook_DocumentRoot docbook_documentroot) {
        this.docbook_documentroot = docbook_documentroot;
    }
    public docbook_ChapterType getDocbook_chaptertype() {
        return docbook_chaptertype;
    }

    public void setDocbook_chaptertype(docbook_ChapterType docbook_chaptertype) {
        this.docbook_chaptertype = docbook_chaptertype;
    }

}