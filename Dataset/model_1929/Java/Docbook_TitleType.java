





import java.util.List;
import java.util.ArrayList;

public class Docbook_TitleType  {

    private String mixed;
    private String group;





    private Docbook_PrefaceType docbook_prefacetype;




    private Docbook_ChapterType docbook_chaptertype;




    private Docbook_ReferenceType docbook_referencetype;




    private Docbook_InfoType docbook_infotype;


    public Docbook_TitleType(
        String mixed,        String group    ) {
        this.mixed = mixed;
        this.group = group;
    }


    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public Docbook_PrefaceType getDocbook_prefacetype() {
        return docbook_prefacetype;
    }

    public void setDocbook_prefacetype(Docbook_PrefaceType docbook_prefacetype) {
        this.docbook_prefacetype = docbook_prefacetype;
    }
    public Docbook_ChapterType getDocbook_chaptertype() {
        return docbook_chaptertype;
    }

    public void setDocbook_chaptertype(Docbook_ChapterType docbook_chaptertype) {
        this.docbook_chaptertype = docbook_chaptertype;
    }
    public Docbook_ReferenceType getDocbook_referencetype() {
        return docbook_referencetype;
    }

    public void setDocbook_referencetype(Docbook_ReferenceType docbook_referencetype) {
        this.docbook_referencetype = docbook_referencetype;
    }
    public Docbook_InfoType getDocbook_infotype() {
        return docbook_infotype;
    }

    public void setDocbook_infotype(Docbook_InfoType docbook_infotype) {
        this.docbook_infotype = docbook_infotype;
    }

}