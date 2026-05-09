





import java.util.List;
import java.util.ArrayList;

public class Docbook_NoteType  {

    private String group;
    private String mixed;





    private Docbook_ChapterType docbook_chaptertype;


    public Docbook_NoteType(
        String group,        String mixed    ) {
        this.group = group;
        this.mixed = mixed;
    }


    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public Docbook_ChapterType getDocbook_chaptertype() {
        return docbook_chaptertype;
    }

    public void setDocbook_chaptertype(Docbook_ChapterType docbook_chaptertype) {
        this.docbook_chaptertype = docbook_chaptertype;
    }

}