





import java.util.List;
import java.util.ArrayList;

public class docbook_Bookinfo extends XMLElement {

    private String pubdate;
    private String date;





    private docbook_Book docbook_book;




    private docbook_Book docbook_book;




    private List<docbook_Author> docbook_authors;




    private docbook_Subtitle docbook_subtitle;




    private docbook_Subtitle docbook_subtitle;




    private docbook_Author docbook_author;


    public docbook_Bookinfo(
        String pubdate,        String date    ) {
        super(
        );
        this.pubdate = pubdate;
        this.date = date;
        this.docbook_authors = new ArrayList<>();
    }

    public docbook_Bookinfo(
        String pubdate,        String date        ArrayList<docbook_Author> docbook_authors    ) {
        this.pubdate = pubdate;
        this.date = date;
        this.docbook_authors = docbook_authors;
    }

    public String getPubdate() {
        return pubdate;
    }

    public void setPubdate(String pubdate) {
        this.pubdate = pubdate;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public docbook_Book getDocbook_book() {
        return docbook_book;
    }

    public void setDocbook_book(docbook_Book docbook_book) {
        this.docbook_book = docbook_book;
    }
    public docbook_Book getDocbook_book() {
        return docbook_book;
    }

    public void setDocbook_book(docbook_Book docbook_book) {
        this.docbook_book = docbook_book;
    }
    public List<docbook_Author> getDocbook_authors() {
        return docbook_authors;
    }

    public void addDocbook_author(Docbook_author docbook_author) {
        this.docbook_authors.add(docbook_author);
    }
    public docbook_Subtitle getDocbook_subtitle() {
        return docbook_subtitle;
    }

    public void setDocbook_subtitle(docbook_Subtitle docbook_subtitle) {
        this.docbook_subtitle = docbook_subtitle;
    }
    public docbook_Subtitle getDocbook_subtitle() {
        return docbook_subtitle;
    }

    public void setDocbook_subtitle(docbook_Subtitle docbook_subtitle) {
        this.docbook_subtitle = docbook_subtitle;
    }
    public docbook_Author getDocbook_author() {
        return docbook_author;
    }

    public void setDocbook_author(docbook_Author docbook_author) {
        this.docbook_author = docbook_author;
    }

}