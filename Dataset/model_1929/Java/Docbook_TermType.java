





import java.util.List;
import java.util.ArrayList;

public class Docbook_TermType  {

    private String mixed;





    private List<Docbook_EnvarType> docbook_envartypes;




    private List<Docbook_FileNameType> docbook_filenametypes;




    private List<Docbook_OptionType> docbook_optiontypes;




    private List<Docbook_EmphasisType> docbook_emphasistypes;


    public Docbook_TermType(
        String mixed    ) {
        this.mixed = mixed;
        this.docbook_envartypes = new ArrayList<>();
        this.docbook_filenametypes = new ArrayList<>();
        this.docbook_optiontypes = new ArrayList<>();
        this.docbook_emphasistypes = new ArrayList<>();
    }

    public Docbook_TermType(
        String mixed        ArrayList<Docbook_EnvarType> docbook_envartypes,        ArrayList<Docbook_FileNameType> docbook_filenametypes,        ArrayList<Docbook_OptionType> docbook_optiontypes,        ArrayList<Docbook_EmphasisType> docbook_emphasistypes    ) {
        this.mixed = mixed;
        this.docbook_envartypes = docbook_envartypes;
        this.docbook_filenametypes = docbook_filenametypes;
        this.docbook_optiontypes = docbook_optiontypes;
        this.docbook_emphasistypes = docbook_emphasistypes;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<Docbook_EnvarType> getDocbook_envartypes() {
        return docbook_envartypes;
    }

    public void addDocbook_envartype(Docbook_envartype docbook_envartype) {
        this.docbook_envartypes.add(docbook_envartype);
    }
    public List<Docbook_FileNameType> getDocbook_filenametypes() {
        return docbook_filenametypes;
    }

    public void addDocbook_filenametype(Docbook_filenametype docbook_filenametype) {
        this.docbook_filenametypes.add(docbook_filenametype);
    }
    public List<Docbook_OptionType> getDocbook_optiontypes() {
        return docbook_optiontypes;
    }

    public void addDocbook_optiontype(Docbook_optiontype docbook_optiontype) {
        this.docbook_optiontypes.add(docbook_optiontype);
    }
    public List<Docbook_EmphasisType> getDocbook_emphasistypes() {
        return docbook_emphasistypes;
    }

    public void addDocbook_emphasistype(Docbook_emphasistype docbook_emphasistype) {
        this.docbook_emphasistypes.add(docbook_emphasistype);
    }

}