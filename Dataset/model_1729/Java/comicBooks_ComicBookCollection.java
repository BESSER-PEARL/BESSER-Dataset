





import java.util.List;
import java.util.ArrayList;

public class comicBooks_ComicBookCollection  {






    private List<comicBooks_Editor> comicbooks_editors;




    private List<comicBooks_Publisher> comicbooks_publishers;




    private List<comicBooks_Artist> comicbooks_artists;




    private List<comicBooks_Series> comicbooks_seriess;




    private List<comicBooks_Writer> comicbooks_writers;


    public comicBooks_ComicBookCollection(
    ) {
        this.comicbooks_editors = new ArrayList<>();
        this.comicbooks_publishers = new ArrayList<>();
        this.comicbooks_artists = new ArrayList<>();
        this.comicbooks_seriess = new ArrayList<>();
        this.comicbooks_writers = new ArrayList<>();
    }

    public comicBooks_ComicBookCollection(
        ArrayList<comicBooks_Editor> comicbooks_editors,        ArrayList<comicBooks_Publisher> comicbooks_publishers,        ArrayList<comicBooks_Artist> comicbooks_artists,        ArrayList<comicBooks_Series> comicbooks_seriess,        ArrayList<comicBooks_Writer> comicbooks_writers    ) {
        this.comicbooks_editors = comicbooks_editors;
        this.comicbooks_publishers = comicbooks_publishers;
        this.comicbooks_artists = comicbooks_artists;
        this.comicbooks_seriess = comicbooks_seriess;
        this.comicbooks_writers = comicbooks_writers;
    }


    public List<comicBooks_Editor> getComicbooks_editors() {
        return comicbooks_editors;
    }

    public void addComicbooks_editor(Comicbooks_editor comicbooks_editor) {
        this.comicbooks_editors.add(comicbooks_editor);
    }
    public List<comicBooks_Publisher> getComicbooks_publishers() {
        return comicbooks_publishers;
    }

    public void addComicbooks_publisher(Comicbooks_publisher comicbooks_publisher) {
        this.comicbooks_publishers.add(comicbooks_publisher);
    }
    public List<comicBooks_Artist> getComicbooks_artists() {
        return comicbooks_artists;
    }

    public void addComicbooks_artist(Comicbooks_artist comicbooks_artist) {
        this.comicbooks_artists.add(comicbooks_artist);
    }
    public List<comicBooks_Series> getComicbooks_seriess() {
        return comicbooks_seriess;
    }

    public void addComicbooks_series(Comicbooks_series comicbooks_series) {
        this.comicbooks_seriess.add(comicbooks_series);
    }
    public List<comicBooks_Writer> getComicbooks_writers() {
        return comicbooks_writers;
    }

    public void addComicbooks_writer(Comicbooks_writer comicbooks_writer) {
        this.comicbooks_writers.add(comicbooks_writer);
    }

}