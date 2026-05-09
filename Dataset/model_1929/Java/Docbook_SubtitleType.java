





import java.util.List;
import java.util.ArrayList;

public class Docbook_SubtitleType  {

    private String mixed;
    private String group;





    private Docbook_InfoType docbook_infotype;




    private List<Docbook_PhraseType> docbook_phrasetypes;




    private List<Docbook_EmphasisType> docbook_emphasistypes;


    public Docbook_SubtitleType(
        String mixed,        String group    ) {
        this.mixed = mixed;
        this.group = group;
        this.docbook_phrasetypes = new ArrayList<>();
        this.docbook_emphasistypes = new ArrayList<>();
    }

    public Docbook_SubtitleType(
        String mixed,        String group        ArrayList<Docbook_PhraseType> docbook_phrasetypes,        ArrayList<Docbook_EmphasisType> docbook_emphasistypes    ) {
        this.mixed = mixed;
        this.group = group;
        this.docbook_phrasetypes = docbook_phrasetypes;
        this.docbook_emphasistypes = docbook_emphasistypes;
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

    public Docbook_InfoType getDocbook_infotype() {
        return docbook_infotype;
    }

    public void setDocbook_infotype(Docbook_InfoType docbook_infotype) {
        this.docbook_infotype = docbook_infotype;
    }
    public List<Docbook_PhraseType> getDocbook_phrasetypes() {
        return docbook_phrasetypes;
    }

    public void addDocbook_phrasetype(Docbook_phrasetype docbook_phrasetype) {
        this.docbook_phrasetypes.add(docbook_phrasetype);
    }
    public List<Docbook_EmphasisType> getDocbook_emphasistypes() {
        return docbook_emphasistypes;
    }

    public void addDocbook_emphasistype(Docbook_emphasistype docbook_emphasistype) {
        this.docbook_emphasistypes.add(docbook_emphasistype);
    }

}