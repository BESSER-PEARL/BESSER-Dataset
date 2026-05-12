





import java.util.List;
import java.util.ArrayList;

public class BIBTEXML_Booklet extends TitledEntry, DatedEntry {

    private String note;
    private String address;
    private String howpublished;





    private List<Author> authors;


    public BIBTEXML_Booklet(
        String note,        String address,        String howpublished    ) {
        super(
        );
        this.note = note;
        this.address = address;
        this.howpublished = howpublished;
        this.authors = new ArrayList<>();
    }

    public BIBTEXML_Booklet(
        String note,        String address,        String howpublished        ArrayList<Author> authors    ) {
        this.note = note;
        this.address = address;
        this.howpublished = howpublished;
        this.authors = authors;
    }

    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getHowpublished() {
        return howpublished;
    }

    public void setHowpublished(String howpublished) {
        this.howpublished = howpublished;
    }

    public List<Author> getAuthors() {
        return authors;
    }

    public void addAuthor(Author author) {
        this.authors.add(author);
    }

}