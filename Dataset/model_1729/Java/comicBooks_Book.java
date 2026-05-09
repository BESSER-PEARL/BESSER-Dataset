





import java.util.List;
import java.util.ArrayList;

public class comicBooks_Book  {

    private String name;
    private String publicationDate;





    private comicBooks_Publisher comicbooks_publisher;




    private comicBooks_Series comicbooks_series;




    private List<comicBooks_Writer> comicbooks_writers;




    private List<comicBooks_Editor> comicbooks_editors;




    private comicBooks_Artist comicbooks_artist;




    private comicBooks_Editor comicbooks_editor;




    private List<comicBooks_Artist> comicbooks_artists;




    private comicBooks_Artist comicbooks_artist;




    private comicBooks_Series comicbooks_series;




    private comicBooks_Artist comicbooks_artist;




    private comicBooks_Writer comicbooks_writer;




    private comicBooks_Publisher comicbooks_publisher;




    private comicBooks_ComicBookCollection comicbooks_comicbookcollection;


    public comicBooks_Book(
        String name,        String publicationDate    ) {
        this.name = name;
        this.publicationDate = publicationDate;
        this.comicbooks_writers = new ArrayList<>();
        this.comicbooks_editors = new ArrayList<>();
        this.comicbooks_artists = new ArrayList<>();
    }

    public comicBooks_Book(
        String name,        String publicationDate        ArrayList<comicBooks_Writer> comicbooks_writers,        ArrayList<comicBooks_Editor> comicbooks_editors,        ArrayList<comicBooks_Artist> comicbooks_artists    ) {
        this.name = name;
        this.publicationDate = publicationDate;
        this.comicbooks_writers = comicbooks_writers;
        this.comicbooks_editors = comicbooks_editors;
        this.comicbooks_artists = comicbooks_artists;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPublicationdate() {
        return publicationDate;
    }

    public void setPublicationdate(String publicationDate) {
        this.publicationDate = publicationDate;
    }

    public comicBooks_Publisher getComicbooks_publisher() {
        return comicbooks_publisher;
    }

    public void setComicbooks_publisher(comicBooks_Publisher comicbooks_publisher) {
        this.comicbooks_publisher = comicbooks_publisher;
    }
    public comicBooks_Series getComicbooks_series() {
        return comicbooks_series;
    }

    public void setComicbooks_series(comicBooks_Series comicbooks_series) {
        this.comicbooks_series = comicbooks_series;
    }
    public List<comicBooks_Writer> getComicbooks_writers() {
        return comicbooks_writers;
    }

    public void addComicbooks_writer(Comicbooks_writer comicbooks_writer) {
        this.comicbooks_writers.add(comicbooks_writer);
    }
    public List<comicBooks_Editor> getComicbooks_editors() {
        return comicbooks_editors;
    }

    public void addComicbooks_editor(Comicbooks_editor comicbooks_editor) {
        this.comicbooks_editors.add(comicbooks_editor);
    }
    public comicBooks_Artist getComicbooks_artist() {
        return comicbooks_artist;
    }

    public void setComicbooks_artist(comicBooks_Artist comicbooks_artist) {
        this.comicbooks_artist = comicbooks_artist;
    }
    public comicBooks_Editor getComicbooks_editor() {
        return comicbooks_editor;
    }

    public void setComicbooks_editor(comicBooks_Editor comicbooks_editor) {
        this.comicbooks_editor = comicbooks_editor;
    }
    public List<comicBooks_Artist> getComicbooks_artists() {
        return comicbooks_artists;
    }

    public void addComicbooks_artist(Comicbooks_artist comicbooks_artist) {
        this.comicbooks_artists.add(comicbooks_artist);
    }
    public comicBooks_Artist getComicbooks_artist() {
        return comicbooks_artist;
    }

    public void setComicbooks_artist(comicBooks_Artist comicbooks_artist) {
        this.comicbooks_artist = comicbooks_artist;
    }
    public comicBooks_Series getComicbooks_series() {
        return comicbooks_series;
    }

    public void setComicbooks_series(comicBooks_Series comicbooks_series) {
        this.comicbooks_series = comicbooks_series;
    }
    public comicBooks_Artist getComicbooks_artist() {
        return comicbooks_artist;
    }

    public void setComicbooks_artist(comicBooks_Artist comicbooks_artist) {
        this.comicbooks_artist = comicbooks_artist;
    }
    public comicBooks_Writer getComicbooks_writer() {
        return comicbooks_writer;
    }

    public void setComicbooks_writer(comicBooks_Writer comicbooks_writer) {
        this.comicbooks_writer = comicbooks_writer;
    }
    public comicBooks_Publisher getComicbooks_publisher() {
        return comicbooks_publisher;
    }

    public void setComicbooks_publisher(comicBooks_Publisher comicbooks_publisher) {
        this.comicbooks_publisher = comicbooks_publisher;
    }
    public comicBooks_ComicBookCollection getComicbooks_comicbookcollection() {
        return comicbooks_comicbookcollection;
    }

    public void setComicbooks_comicbookcollection(comicBooks_ComicBookCollection comicbooks_comicbookcollection) {
        this.comicbooks_comicbookcollection = comicbooks_comicbookcollection;
    }

}