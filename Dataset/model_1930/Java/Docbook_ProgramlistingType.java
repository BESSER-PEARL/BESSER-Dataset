





import java.util.List;
import java.util.ArrayList;

public class Docbook_ProgramlistingType  {

    private String superscript;
    private String group;
    private String mixed;
    private String linenumbering;
    private String format;
    private String language;





    private Docbook_SectionType docbook_sectiontype;




    private List<Docbook_PhraseType> docbook_phrasetypes;




    private Docbook_EntryType docbook_entrytype;




    private Docbook_DocumentRoot docbook_documentroot;




    private List<Docbook_EmphasisType> docbook_emphasistypes;


    public Docbook_ProgramlistingType(
        String superscript,        String group,        String mixed,        String linenumbering,        String format,        String language    ) {
        this.superscript = superscript;
        this.group = group;
        this.mixed = mixed;
        this.linenumbering = linenumbering;
        this.format = format;
        this.language = language;
        this.docbook_phrasetypes = new ArrayList<>();
        this.docbook_emphasistypes = new ArrayList<>();
    }

    public Docbook_ProgramlistingType(
        String superscript,        String group,        String mixed,        String linenumbering,        String format,        String language        ArrayList<Docbook_PhraseType> docbook_phrasetypes,        ArrayList<Docbook_EmphasisType> docbook_emphasistypes    ) {
        this.superscript = superscript;
        this.group = group;
        this.mixed = mixed;
        this.linenumbering = linenumbering;
        this.format = format;
        this.language = language;
        this.docbook_phrasetypes = docbook_phrasetypes;
        this.docbook_emphasistypes = docbook_emphasistypes;
    }

    public String getSuperscript() {
        return superscript;
    }

    public void setSuperscript(String superscript) {
        this.superscript = superscript;
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
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
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

}