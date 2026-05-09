





import java.util.List;
import java.util.ArrayList;

public class bookstore_Cd extends Ent {

    private String bandArtist;
    private String albumName;





    private List<bookstore_Person> bookstore_persons;


    public bookstore_Cd(
        String bandArtist,        String albumName    ) {
        super(
        );
        this.bandArtist = bandArtist;
        this.albumName = albumName;
        this.bookstore_persons = new ArrayList<>();
    }

    public bookstore_Cd(
        String bandArtist,        String albumName        ArrayList<bookstore_Person> bookstore_persons    ) {
        this.bandArtist = bandArtist;
        this.albumName = albumName;
        this.bookstore_persons = bookstore_persons;
    }

    public String getBandartist() {
        return bandArtist;
    }

    public void setBandartist(String bandArtist) {
        this.bandArtist = bandArtist;
    }
    public String getAlbumname() {
        return albumName;
    }

    public void setAlbumname(String albumName) {
        this.albumName = albumName;
    }

    public List<bookstore_Person> getBookstore_persons() {
        return bookstore_persons;
    }

    public void addBookstore_person(Bookstore_person bookstore_person) {
        this.bookstore_persons.add(bookstore_person);
    }

}