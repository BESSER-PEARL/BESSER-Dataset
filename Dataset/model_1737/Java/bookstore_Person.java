





import java.util.List;
import java.util.ArrayList;

public class bookstore_Person extends Ent {

    private String voornaam;
    private String achternaam;





    private bookstore_Person bookstore_person;


    public bookstore_Person(
        String voornaam,        String achternaam    ) {
        super(
        );
        this.voornaam = voornaam;
        this.achternaam = achternaam;
    }


    public String getVoornaam() {
        return voornaam;
    }

    public void setVoornaam(String voornaam) {
        this.voornaam = voornaam;
    }
    public String getAchternaam() {
        return achternaam;
    }

    public void setAchternaam(String achternaam) {
        this.achternaam = achternaam;
    }

    public bookstore_Person getBookstore_person() {
        return bookstore_person;
    }

    public void setBookstore_person(bookstore_Person bookstore_person) {
        this.bookstore_person = bookstore_person;
    }

}