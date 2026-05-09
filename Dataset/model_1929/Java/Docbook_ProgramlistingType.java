





import java.util.List;
import java.util.ArrayList;

public class Docbook_ProgramlistingType  {

    private String language;
    private String mixed;
    private String superscript;
    private String linenumbering;
    private String format;
    private String group;





    private Docbook_DocumentRoot docbook_documentroot;




    private List<Docbook_EmphasisType> docbook_emphasistypes;




    private Docbook_SectionType docbook_sectiontype;




    private List<Docbook_PhraseType> docbook_phrasetypes;




    private Docbook_EntryType docbook_entrytype;


    public Docbook_ProgramlistingType(
        String language,        String mixed,        String superscript,        String linenumbering,        String format,        String group    ) {
        this.language = language;
        this.mixed = mixed;
        this.superscript = superscript;
        this.linenumbering = linenumbering;
        this.format = format;
        this.group = group;
        this.docbook_emphasistypes = new ArrayList<>();
        this.docbook_phrasetypes = new ArrayList<>();
    }

    public Docbook_ProgramlistingType(
        String language,        String mixed,        String superscript,        String linenumbering,        String format,        String group        ArrayList<Docbook_EmphasisType> docbook_emphasistypes,        ArrayList<Docbook_PhraseType> docbook_phrasetypes    ) {
        this.language = language;
        this.mixed = mixed;
        this.superscript = superscript;
        this.linenumbering = linenumbering;
        this.format = format;
        this.group = group;
        this.docbook_emphasistypes = docbook_emphasistypes;
        this.docbook_phrasetypes = docbook_phrasetypes;
    }

    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getSuperscript() {
        return superscript;
    }

    public void setSuperscript(String superscript) {
        this.superscript = superscript;
    }
    public String getLinenumbering() {
        return linenumbering;
    }

    public void setLinenumbering(String linenumbering) {
        this.linenumbering = linenumbering;
    }
    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public Docbook_DocumentRoot getDocbook_documentroot() {
        return docbook_documentroot;
    }

    public void setDocbook_documentroot(Docbook_DocumentRoot docbook_documentroot) {
        this.docbook_documentroot = docbook_documentroot;
    }
    public List<Docbook_EmphasisType> getDocbook_emphasistypes() {
        return docbook_emphasistypes;
    }

    public void addDocbook_emphasistype(Docbook_emphasistype docbook_emphasistype) {
        this.docbook_emphasistypes.add(docbook_emphasistype);
    }
    public Docbook_SectionType getDocbook_sectiontype() {
        return docbook_sectiontype;
    }

    public void setDocbook_sectiontype(Docbook_SectionType docbook_sectiontype) {
        this.docbook_sectiontype = docbook_sectiontype;
    }
    public List<Docbook_PhraseType> getDocbook_phrasetypes() {
        return docbook_phrasetypes;
    }

    public void addDocbook_phrasetype(Docbook_phrasetype docbook_phrasetype) {
        this.docbook_phrasetypes.add(docbook_phrasetype);
    }
    public Docbook_EntryType getDocbook_entrytype() {
        return docbook_entrytype;
    }

    public void setDocbook_entrytype(Docbook_EntryType docbook_entrytype) {
        this.docbook_entrytype = docbook_entrytype;
    }

}