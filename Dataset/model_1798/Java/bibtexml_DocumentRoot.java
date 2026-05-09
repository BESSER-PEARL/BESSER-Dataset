





import java.util.List;
import java.util.ArrayList;

public class bibtexml_DocumentRoot  {

    private String mixed;
    private String year;
    private String edition;
    private String series;
    private String title;
    private String key;
    private String institution;
    private String url;
    private String annote;
    private String chapter;
    private String journal;
    private String howpublished;
    private String note;
    private String crossref;
    private String organization;
    private String author;
    private String address;
    private String school;
    private String number;
    private String month;
    private String editor;
    private String type;
    private String volume;
    private String publisher;
    private String doi;
    private String pages;
    private String booktitle;





    private List<bibtexml_InproceedingsType> bibtexml_inproceedingstypes;




    private List<bibtexml_InbookType> bibtexml_inbooktypes;




    private List<bibtexml_ManualType> bibtexml_manualtypes;




    private List<bibtexml_MastersthesisType> bibtexml_mastersthesistypes;




    private List<bibtexml_PhdthesisType> bibtexml_phdthesistypes;




    private List<bibtexml_ProceedingsType> bibtexml_proceedingstypes;




    private List<bibtexml_BookletType> bibtexml_booklettypes;




    private List<bibtexml_UnpublishedType> bibtexml_unpublishedtypes;




    private List<bibtexml_ArticleType> bibtexml_articletypes;




    private List<bibtexml_BibTeXMLEntryType> bibtexml_bibtexmlentrytypes;




    private List<bibtexml_ConferenceType> bibtexml_conferencetypes;




    private List<bibtexml_BookType> bibtexml_booktypes;




    private List<bibtexml_IncollectionType> bibtexml_incollectiontypes;




    private List<bibtexml_TechreportType> bibtexml_techreporttypes;




    private List<bibtexml_MiscType> bibtexml_misctypes;


    public bibtexml_DocumentRoot(
        String mixed,        String year,        String edition,        String series,        String title,        String key,        String institution,        String url,        String annote,        String chapter,        String journal,        String howpublished,        String note,        String crossref,        String organization,        String author,        String address,        String school,        String number,        String month,        String editor,        String type,        String volume,        String publisher,        String doi,        String pages,        String booktitle    ) {
        this.mixed = mixed;
        this.year = year;
        this.edition = edition;
        this.series = series;
        this.title = title;
        this.key = key;
        this.institution = institution;
        this.url = url;
        this.annote = annote;
        this.chapter = chapter;
        this.journal = journal;
        this.howpublished = howpublished;
        this.note = note;
        this.crossref = crossref;
        this.organization = organization;
        this.author = author;
        this.address = address;
        this.school = school;
        this.number = number;
        this.month = month;
        this.editor = editor;
        this.type = type;
        this.volume = volume;
        this.publisher = publisher;
        this.doi = doi;
        this.pages = pages;
        this.booktitle = booktitle;
        this.bibtexml_inproceedingstypes = new ArrayList<>();
        this.bibtexml_inbooktypes = new ArrayList<>();
        this.bibtexml_manualtypes = new ArrayList<>();
        this.bibtexml_mastersthesistypes = new ArrayList<>();
        this.bibtexml_phdthesistypes = new ArrayList<>();
        this.bibtexml_proceedingstypes = new ArrayList<>();
        this.bibtexml_booklettypes = new ArrayList<>();
        this.bibtexml_unpublishedtypes = new ArrayList<>();
        this.bibtexml_articletypes = new ArrayList<>();
        this.bibtexml_bibtexmlentrytypes = new ArrayList<>();
        this.bibtexml_conferencetypes = new ArrayList<>();
        this.bibtexml_booktypes = new ArrayList<>();
        this.bibtexml_incollectiontypes = new ArrayList<>();
        this.bibtexml_techreporttypes = new ArrayList<>();
        this.bibtexml_misctypes = new ArrayList<>();
    }

    public bibtexml_DocumentRoot(
        String mixed,        String year,        String edition,        String series,        String title,        String key,        String institution,        String url,        String annote,        String chapter,        String journal,        String howpublished,        String note,        String crossref,        String organization,        String author,        String address,        String school,        String number,        String month,        String editor,        String type,        String volume,        String publisher,        String doi,        String pages,        String booktitle        ArrayList<bibtexml_InproceedingsType> bibtexml_inproceedingstypes,        ArrayList<bibtexml_InbookType> bibtexml_inbooktypes,        ArrayList<bibtexml_ManualType> bibtexml_manualtypes,        ArrayList<bibtexml_MastersthesisType> bibtexml_mastersthesistypes,        ArrayList<bibtexml_PhdthesisType> bibtexml_phdthesistypes,        ArrayList<bibtexml_ProceedingsType> bibtexml_proceedingstypes,        ArrayList<bibtexml_BookletType> bibtexml_booklettypes,        ArrayList<bibtexml_UnpublishedType> bibtexml_unpublishedtypes,        ArrayList<bibtexml_ArticleType> bibtexml_articletypes,        ArrayList<bibtexml_BibTeXMLEntryType> bibtexml_bibtexmlentrytypes,        ArrayList<bibtexml_ConferenceType> bibtexml_conferencetypes,        ArrayList<bibtexml_BookType> bibtexml_booktypes,        ArrayList<bibtexml_IncollectionType> bibtexml_incollectiontypes,        ArrayList<bibtexml_TechreportType> bibtexml_techreporttypes,        ArrayList<bibtexml_MiscType> bibtexml_misctypes    ) {
        this.mixed = mixed;
        this.year = year;
        this.edition = edition;
        this.series = series;
        this.title = title;
        this.key = key;
        this.institution = institution;
        this.url = url;
        this.annote = annote;
        this.chapter = chapter;
        this.journal = journal;
        this.howpublished = howpublished;
        this.note = note;
        this.crossref = crossref;
        this.organization = organization;
        this.author = author;
        this.address = address;
        this.school = school;
        this.number = number;
        this.month = month;
        this.editor = editor;
        this.type = type;
        this.volume = volume;
        this.publisher = publisher;
        this.doi = doi;
        this.pages = pages;
        this.booktitle = booktitle;
        this.bibtexml_inproceedingstypes = bibtexml_inproceedingstypes;
        this.bibtexml_inbooktypes = bibtexml_inbooktypes;
        this.bibtexml_manualtypes = bibtexml_manualtypes;
        this.bibtexml_mastersthesistypes = bibtexml_mastersthesistypes;
        this.bibtexml_phdthesistypes = bibtexml_phdthesistypes;
        this.bibtexml_proceedingstypes = bibtexml_proceedingstypes;
        this.bibtexml_booklettypes = bibtexml_booklettypes;
        this.bibtexml_unpublishedtypes = bibtexml_unpublishedtypes;
        this.bibtexml_articletypes = bibtexml_articletypes;
        this.bibtexml_bibtexmlentrytypes = bibtexml_bibtexmlentrytypes;
        this.bibtexml_conferencetypes = bibtexml_conferencetypes;
        this.bibtexml_booktypes = bibtexml_booktypes;
        this.bibtexml_incollectiontypes = bibtexml_incollectiontypes;
        this.bibtexml_techreporttypes = bibtexml_techreporttypes;
        this.bibtexml_misctypes = bibtexml_misctypes;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }
    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }
    public String getEdition() {
        return edition;
    }

    public void setEdition(String edition) {
        this.edition = edition;
    }
    public String getSeries() {
        return series;
    }

    public void setSeries(String series) {
        this.series = series;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getInstitution() {
        return institution;
    }

    public void setInstitution(String institution) {
        this.institution = institution;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }
    public String getAnnote() {
        return annote;
    }

    public void setAnnote(String annote) {
        this.annote = annote;
    }
    public String getChapter() {
        return chapter;
    }

    public void setChapter(String chapter) {
        this.chapter = chapter;
    }
    public String getJournal() {
        return journal;
    }

    public void setJournal(String journal) {
        this.journal = journal;
    }
    public String getHowpublished() {
        return howpublished;
    }

    public void setHowpublished(String howpublished) {
        this.howpublished = howpublished;
    }
    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }
    public String getCrossref() {
        return crossref;
    }

    public void setCrossref(String crossref) {
        this.crossref = crossref;
    }
    public String getOrganization() {
        return organization;
    }

    public void setOrganization(String organization) {
        this.organization = organization;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getSchool() {
        return school;
    }

    public void setSchool(String school) {
        this.school = school;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public String getEditor() {
        return editor;
    }

    public void setEditor(String editor) {
        this.editor = editor;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getVolume() {
        return volume;
    }

    public void setVolume(String volume) {
        this.volume = volume;
    }
    public String getPublisher() {
        return publisher;
    }

    public void setPublisher(String publisher) {
        this.publisher = publisher;
    }
    public String getDoi() {
        return doi;
    }

    public void setDoi(String doi) {
        this.doi = doi;
    }
    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }
    public String getBooktitle() {
        return booktitle;
    }

    public void setBooktitle(String booktitle) {
        this.booktitle = booktitle;
    }

    public List<bibtexml_InproceedingsType> getBibtexml_inproceedingstypes() {
        return bibtexml_inproceedingstypes;
    }

    public void addBibtexml_inproceedingstype(Bibtexml_inproceedingstype bibtexml_inproceedingstype) {
        this.bibtexml_inproceedingstypes.add(bibtexml_inproceedingstype);
    }
    public List<bibtexml_InbookType> getBibtexml_inbooktypes() {
        return bibtexml_inbooktypes;
    }

    public void addBibtexml_inbooktype(Bibtexml_inbooktype bibtexml_inbooktype) {
        this.bibtexml_inbooktypes.add(bibtexml_inbooktype);
    }
    public List<bibtexml_ManualType> getBibtexml_manualtypes() {
        return bibtexml_manualtypes;
    }

    public void addBibtexml_manualtype(Bibtexml_manualtype bibtexml_manualtype) {
        this.bibtexml_manualtypes.add(bibtexml_manualtype);
    }
    public List<bibtexml_MastersthesisType> getBibtexml_mastersthesistypes() {
        return bibtexml_mastersthesistypes;
    }

    public void addBibtexml_mastersthesistype(Bibtexml_mastersthesistype bibtexml_mastersthesistype) {
        this.bibtexml_mastersthesistypes.add(bibtexml_mastersthesistype);
    }
    public List<bibtexml_PhdthesisType> getBibtexml_phdthesistypes() {
        return bibtexml_phdthesistypes;
    }

    public void addBibtexml_phdthesistype(Bibtexml_phdthesistype bibtexml_phdthesistype) {
        this.bibtexml_phdthesistypes.add(bibtexml_phdthesistype);
    }
    public List<bibtexml_ProceedingsType> getBibtexml_proceedingstypes() {
        return bibtexml_proceedingstypes;
    }

    public void addBibtexml_proceedingstype(Bibtexml_proceedingstype bibtexml_proceedingstype) {
        this.bibtexml_proceedingstypes.add(bibtexml_proceedingstype);
    }
    public List<bibtexml_BookletType> getBibtexml_booklettypes() {
        return bibtexml_booklettypes;
    }

    public void addBibtexml_booklettype(Bibtexml_booklettype bibtexml_booklettype) {
        this.bibtexml_booklettypes.add(bibtexml_booklettype);
    }
    public List<bibtexml_UnpublishedType> getBibtexml_unpublishedtypes() {
        return bibtexml_unpublishedtypes;
    }

    public void addBibtexml_unpublishedtype(Bibtexml_unpublishedtype bibtexml_unpublishedtype) {
        this.bibtexml_unpublishedtypes.add(bibtexml_unpublishedtype);
    }
    public List<bibtexml_ArticleType> getBibtexml_articletypes() {
        return bibtexml_articletypes;
    }

    public void addBibtexml_articletype(Bibtexml_articletype bibtexml_articletype) {
        this.bibtexml_articletypes.add(bibtexml_articletype);
    }
    public List<bibtexml_BibTeXMLEntryType> getBibtexml_bibtexmlentrytypes() {
        return bibtexml_bibtexmlentrytypes;
    }

    public void addBibtexml_bibtexmlentrytype(Bibtexml_bibtexmlentrytype bibtexml_bibtexmlentrytype) {
        this.bibtexml_bibtexmlentrytypes.add(bibtexml_bibtexmlentrytype);
    }
    public List<bibtexml_ConferenceType> getBibtexml_conferencetypes() {
        return bibtexml_conferencetypes;
    }

    public void addBibtexml_conferencetype(Bibtexml_conferencetype bibtexml_conferencetype) {
        this.bibtexml_conferencetypes.add(bibtexml_conferencetype);
    }
    public List<bibtexml_BookType> getBibtexml_booktypes() {
        return bibtexml_booktypes;
    }

    public void addBibtexml_booktype(Bibtexml_booktype bibtexml_booktype) {
        this.bibtexml_booktypes.add(bibtexml_booktype);
    }
    public List<bibtexml_IncollectionType> getBibtexml_incollectiontypes() {
        return bibtexml_incollectiontypes;
    }

    public void addBibtexml_incollectiontype(Bibtexml_incollectiontype bibtexml_incollectiontype) {
        this.bibtexml_incollectiontypes.add(bibtexml_incollectiontype);
    }
    public List<bibtexml_TechreportType> getBibtexml_techreporttypes() {
        return bibtexml_techreporttypes;
    }

    public void addBibtexml_techreporttype(Bibtexml_techreporttype bibtexml_techreporttype) {
        this.bibtexml_techreporttypes.add(bibtexml_techreporttype);
    }
    public List<bibtexml_MiscType> getBibtexml_misctypes() {
        return bibtexml_misctypes;
    }

    public void addBibtexml_misctype(Bibtexml_misctype bibtexml_misctype) {
        this.bibtexml_misctypes.add(bibtexml_misctype);
    }

}