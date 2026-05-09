





import java.util.List;
import java.util.ArrayList;

public class Docbook_DocumentRoot  {

    private String state;
    private String superscript;
    private String confnum;
    private String keyword;
    private String conftitle;
    private String bibliomisc;
    private String caution;
    private String firstname;
    private String confsponsor;
    private String pubdate;
    private String mixed;
    private String warning;
    private String subtitle;
    private String date;
    private String publishername;





    private List<Docbook_BookType> docbook_booktypes;




    private List<Docbook_AbstractType> docbook_abstracttypes;




    private List<Docbook_AddressType> docbook_addresstypes;




    private List<Docbook_ColspecType> docbook_colspectypes;




    private List<Docbook_ConfgroupType> docbook_confgrouptypes;




    private List<Docbook_InfoType> docbook_infotypes;




    private List<Docbook_PrefaceType> docbook_prefacetypes;




    private List<Docbook_OtheraddrType> docbook_otheraddrtypes;




    private List<Docbook_ParaType> docbook_paratypes;




    private List<Docbook_AuthorType> docbook_authortypes;




    private List<Docbook_TitleType> docbook_titletypes;




    private List<Docbook_SectionType> docbook_sectiontypes;




    private List<Docbook_NoteType> docbook_notetypes;




    private List<Docbook_ChapterType> docbook_chaptertypes;


    public Docbook_DocumentRoot(
        String state,        String superscript,        String confnum,        String keyword,        String conftitle,        String bibliomisc,        String caution,        String firstname,        String confsponsor,        String pubdate,        String mixed,        String warning,        String subtitle,        String date,        String publishername    ) {
        this.state = state;
        this.superscript = superscript;
        this.confnum = confnum;
        this.keyword = keyword;
        this.conftitle = conftitle;
        this.bibliomisc = bibliomisc;
        this.caution = caution;
        this.firstname = firstname;
        this.confsponsor = confsponsor;
        this.pubdate = pubdate;
        this.mixed = mixed;
        this.warning = warning;
        this.subtitle = subtitle;
        this.date = date;
        this.publishername = publishername;
        this.docbook_booktypes = new ArrayList<>();
        this.docbook_abstracttypes = new ArrayList<>();
        this.docbook_addresstypes = new ArrayList<>();
        this.docbook_colspectypes = new ArrayList<>();
        this.docbook_confgrouptypes = new ArrayList<>();
        this.docbook_infotypes = new ArrayList<>();
        this.docbook_prefacetypes = new ArrayList<>();
        this.docbook_otheraddrtypes = new ArrayList<>();
        this.docbook_paratypes = new ArrayList<>();
        this.docbook_authortypes = new ArrayList<>();
        this.docbook_titletypes = new ArrayList<>();
        this.docbook_sectiontypes = new ArrayList<>();
        this.docbook_notetypes = new ArrayList<>();
        this.docbook_chaptertypes = new ArrayList<>();
    }

    public Docbook_DocumentRoot(
        String state,        String superscript,        String confnum,        String keyword,        String conftitle,        String bibliomisc,        String caution,        String firstname,        String confsponsor,        String pubdate,        String mixed,        String warning,        String subtitle,        String date,        String publishername        ArrayList<Docbook_BookType> docbook_booktypes,        ArrayList<Docbook_AbstractType> docbook_abstracttypes,        ArrayList<Docbook_AddressType> docbook_addresstypes,        ArrayList<Docbook_ColspecType> docbook_colspectypes,        ArrayList<Docbook_ConfgroupType> docbook_confgrouptypes,        ArrayList<Docbook_InfoType> docbook_infotypes,        ArrayList<Docbook_PrefaceType> docbook_prefacetypes,        ArrayList<Docbook_OtheraddrType> docbook_otheraddrtypes,        ArrayList<Docbook_ParaType> docbook_paratypes,        ArrayList<Docbook_AuthorType> docbook_authortypes,        ArrayList<Docbook_TitleType> docbook_titletypes,        ArrayList<Docbook_SectionType> docbook_sectiontypes,        ArrayList<Docbook_NoteType> docbook_notetypes,        ArrayList<Docbook_ChapterType> docbook_chaptertypes    ) {
        this.state = state;
        this.superscript = superscript;
        this.confnum = confnum;
        this.keyword = keyword;
        this.conftitle = conftitle;
        this.bibliomisc = bibliomisc;
        this.caution = caution;
        this.firstname = firstname;
        this.confsponsor = confsponsor;
        this.pubdate = pubdate;
        this.mixed = mixed;
        this.warning = warning;
        this.subtitle = subtitle;
        this.date = date;
        this.publishername = publishername;
        this.docbook_booktypes = docbook_booktypes;
        this.docbook_abstracttypes = docbook_abstracttypes;
        this.docbook_addresstypes = docbook_addresstypes;
        this.docbook_colspectypes = docbook_colspectypes;
        this.docbook_confgrouptypes = docbook_confgrouptypes;
        this.docbook_infotypes = docbook_infotypes;
        this.docbook_prefacetypes = docbook_prefacetypes;
        this.docbook_otheraddrtypes = docbook_otheraddrtypes;
        this.docbook_paratypes = docbook_paratypes;
        this.docbook_authortypes = docbook_authortypes;
        this.docbook_titletypes = docbook_titletypes;
        this.docbook_sectiontypes = docbook_sectiontypes;
        this.docbook_notetypes = docbook_notetypes;
        this.docbook_chaptertypes = docbook_chaptertypes;
    }

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getSuperscript() {
        return superscript;
    }

    public void setSuperscript(String superscript) {
        this.superscript = superscript;
    }
    public String getConfnum() {
        return confnum;
    }

    public void setConfnum(String confnum) {
        this.confnum = confnum;
    }
    public String getKeyword() {
        return keyword;
    }

    public void setKeyword(String keyword) {
        this.keyword = keyword;
    }
    public String getConftitle() {
        return conftitle;
    }

    public void setConftitle(String conftitle) {
        this.conftitle = conftitle;
    }
    public String getBibliomisc() {
        return bibliomisc;
    }

    public void setBibliomisc(String bibliomisc) {
        this.bibliomisc = bibliomisc;
    }
    public String getCaution() {
        return caution;
    }

    public void setCaution(String caution) {
        this.caution = caution;
    }
    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }
    public String getConfsponsor() {
        return confsponsor;
    }

    public void setConfsponsor(String confsponsor) {
        this.confsponsor = confsponsor;
    }
    public String getPubdate() {
        return pubdate;
    }

    public void setPubdate(String pubdate) {
        this.pubdate = pubdate;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getWarning() {
        return warning;
    }

    public void setWarning(String warning) {
        this.warning = warning;
    }
    public String getSubtitle() {
        return subtitle;
    }

    public void setSubtitle(String subtitle) {
        this.subtitle = subtitle;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getPublishername() {
        return publishername;
    }

    public void setPublishername(String publishername) {
        this.publishername = publishername;
    }

    public List<Docbook_BookType> getDocbook_booktypes() {
        return docbook_booktypes;
    }

    public void addDocbook_booktype(Docbook_booktype docbook_booktype) {
        this.docbook_booktypes.add(docbook_booktype);
    }
    public List<Docbook_AbstractType> getDocbook_abstracttypes() {
        return docbook_abstracttypes;
    }

    public void addDocbook_abstracttype(Docbook_abstracttype docbook_abstracttype) {
        this.docbook_abstracttypes.add(docbook_abstracttype);
    }
    public List<Docbook_AddressType> getDocbook_addresstypes() {
        return docbook_addresstypes;
    }

    public void addDocbook_addresstype(Docbook_addresstype docbook_addresstype) {
        this.docbook_addresstypes.add(docbook_addresstype);
    }
    public List<Docbook_ColspecType> getDocbook_colspectypes() {
        return docbook_colspectypes;
    }

    public void addDocbook_colspectype(Docbook_colspectype docbook_colspectype) {
        this.docbook_colspectypes.add(docbook_colspectype);
    }
    public List<Docbook_ConfgroupType> getDocbook_confgrouptypes() {
        return docbook_confgrouptypes;
    }

    public void addDocbook_confgrouptype(Docbook_confgrouptype docbook_confgrouptype) {
        this.docbook_confgrouptypes.add(docbook_confgrouptype);
    }
    public List<Docbook_InfoType> getDocbook_infotypes() {
        return docbook_infotypes;
    }

    public void addDocbook_infotype(Docbook_infotype docbook_infotype) {
        this.docbook_infotypes.add(docbook_infotype);
    }
    public List<Docbook_PrefaceType> getDocbook_prefacetypes() {
        return docbook_prefacetypes;
    }

    public void addDocbook_prefacetype(Docbook_prefacetype docbook_prefacetype) {
        this.docbook_prefacetypes.add(docbook_prefacetype);
    }
    public List<Docbook_OtheraddrType> getDocbook_otheraddrtypes() {
        return docbook_otheraddrtypes;
    }

    public void addDocbook_otheraddrtype(Docbook_otheraddrtype docbook_otheraddrtype) {
        this.docbook_otheraddrtypes.add(docbook_otheraddrtype);
    }
    public List<Docbook_ParaType> getDocbook_paratypes() {
        return docbook_paratypes;
    }

    public void addDocbook_paratype(Docbook_paratype docbook_paratype) {
        this.docbook_paratypes.add(docbook_paratype);
    }
    public List<Docbook_AuthorType> getDocbook_authortypes() {
        return docbook_authortypes;
    }

    public void addDocbook_authortype(Docbook_authortype docbook_authortype) {
        this.docbook_authortypes.add(docbook_authortype);
    }
    public List<Docbook_TitleType> getDocbook_titletypes() {
        return docbook_titletypes;
    }

    public void addDocbook_titletype(Docbook_titletype docbook_titletype) {
        this.docbook_titletypes.add(docbook_titletype);
    }
    public List<Docbook_SectionType> getDocbook_sectiontypes() {
        return docbook_sectiontypes;
    }

    public void addDocbook_sectiontype(Docbook_sectiontype docbook_sectiontype) {
        this.docbook_sectiontypes.add(docbook_sectiontype);
    }
    public List<Docbook_NoteType> getDocbook_notetypes() {
        return docbook_notetypes;
    }

    public void addDocbook_notetype(Docbook_notetype docbook_notetype) {
        this.docbook_notetypes.add(docbook_notetype);
    }
    public List<Docbook_ChapterType> getDocbook_chaptertypes() {
        return docbook_chaptertypes;
    }

    public void addDocbook_chaptertype(Docbook_chaptertype docbook_chaptertype) {
        this.docbook_chaptertypes.add(docbook_chaptertype);
    }

}