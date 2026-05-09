





import java.util.List;
import java.util.ArrayList;

public class Docbook_SectionType  {

    private String annotations;
    private String group;
    private String caution;
    private String warning;





    private List<Docbook_ParaType> docbook_paratypes;




    private Docbook_ChapterType docbook_chaptertype;




    private List<Docbook_NoteType> docbook_notetypes;




    private List<Docbook_TitleType> docbook_titletypes;




    private Docbook_SectionType docbook_sectiontype;


    public Docbook_SectionType(
        String annotations,        String group,        String caution,        String warning    ) {
        this.annotations = annotations;
        this.group = group;
        this.caution = caution;
        this.warning = warning;
        this.docbook_paratypes = new ArrayList<>();
        this.docbook_notetypes = new ArrayList<>();
        this.docbook_titletypes = new ArrayList<>();
    }

    public Docbook_SectionType(
        String annotations,        String group,        String caution,        String warning        ArrayList<Docbook_ParaType> docbook_paratypes,        ArrayList<Docbook_NoteType> docbook_notetypes,        ArrayList<Docbook_TitleType> docbook_titletypes    ) {
        this.annotations = annotations;
        this.group = group;
        this.caution = caution;
        this.warning = warning;
        this.docbook_paratypes = docbook_paratypes;
        this.docbook_notetypes = docbook_notetypes;
        this.docbook_titletypes = docbook_titletypes;
    }

    public String getAnnotations() {
        return annotations;
    }

    public void setAnnotations(String annotations) {
        this.annotations = annotations;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }
    public String getCaution() {
        return caution;
    }

    public void setCaution(String caution) {
        this.caution = caution;
    }
    public String getWarning() {
        return warning;
    }

    public void setWarning(String warning) {
        this.warning = warning;
    }

    public List<Docbook_ParaType> getDocbook_paratypes() {
        return docbook_paratypes;
    }

    public void addDocbook_paratype(Docbook_paratype docbook_paratype) {
        this.docbook_paratypes.add(docbook_paratype);
    }
    public Docbook_ChapterType getDocbook_chaptertype() {
        return docbook_chaptertype;
    }

    public void setDocbook_chaptertype(Docbook_ChapterType docbook_chaptertype) {
        this.docbook_chaptertype = docbook_chaptertype;
    }
    public List<Docbook_NoteType> getDocbook_notetypes() {
        return docbook_notetypes;
    }

    public void addDocbook_notetype(Docbook_notetype docbook_notetype) {
        this.docbook_notetypes.add(docbook_notetype);
    }
    public List<Docbook_TitleType> getDocbook_titletypes() {
        return docbook_titletypes;
    }

    public void addDocbook_titletype(Docbook_titletype docbook_titletype) {
        this.docbook_titletypes.add(docbook_titletype);
    }
    public Docbook_SectionType getDocbook_sectiontype() {
        return docbook_sectiontype;
    }

    public void setDocbook_sectiontype(Docbook_SectionType docbook_sectiontype) {
        this.docbook_sectiontype = docbook_sectiontype;
    }

}