





import java.util.List;
import java.util.ArrayList;

public class Docbook_InfoType  {

    private String pubdate;
    private String bibliomisc;
    private String releaseinfo;
    private String date;
    private String productname;
    private String group;





    private List<Docbook_AuthorType> docbook_authortypes;




    private Docbook_AbstractType docbook_abstracttype;




    private Docbook_BookType docbook_booktype;


    public Docbook_InfoType(
        String pubdate,        String bibliomisc,        String releaseinfo,        String date,        String productname,        String group    ) {
        this.pubdate = pubdate;
        this.bibliomisc = bibliomisc;
        this.releaseinfo = releaseinfo;
        this.date = date;
        this.productname = productname;
        this.group = group;
        this.docbook_authortypes = new ArrayList<>();
    }

    public Docbook_InfoType(
        String pubdate,        String bibliomisc,        String releaseinfo,        String date,        String productname,        String group        ArrayList<Docbook_AuthorType> docbook_authortypes    ) {
        this.pubdate = pubdate;
        this.bibliomisc = bibliomisc;
        this.releaseinfo = releaseinfo;
        this.date = date;
        this.productname = productname;
        this.group = group;
        this.docbook_authortypes = docbook_authortypes;
    }

    public String getPubdate() {
        return pubdate;
    }

    public void setPubdate(String pubdate) {
        this.pubdate = pubdate;
    }
    public String getBibliomisc() {
        return bibliomisc;
    }

    public void setBibliomisc(String bibliomisc) {
        this.bibliomisc = bibliomisc;
    }
    public String getReleaseinfo() {
        return releaseinfo;
    }

    public void setReleaseinfo(String releaseinfo) {
        this.releaseinfo = releaseinfo;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getProductname() {
        return productname;
    }

    public void setProductname(String productname) {
        this.productname = productname;
    }
    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public List<Docbook_AuthorType> getDocbook_authortypes() {
        return docbook_authortypes;
    }

    public void addDocbook_authortype(Docbook_authortype docbook_authortype) {
        this.docbook_authortypes.add(docbook_authortype);
    }
    public Docbook_AbstractType getDocbook_abstracttype() {
        return docbook_abstracttype;
    }

    public void setDocbook_abstracttype(Docbook_AbstractType docbook_abstracttype) {
        this.docbook_abstracttype = docbook_abstracttype;
    }
    public Docbook_BookType getDocbook_booktype() {
        return docbook_booktype;
    }

    public void setDocbook_booktype(Docbook_BookType docbook_booktype) {
        this.docbook_booktype = docbook_booktype;
    }

}