





import java.util.List;
import java.util.ArrayList;

public class Bibtex_Entry  {

    private String id;
    private String title;





    private Bibtex_Author bibtex_author;




    private Bibtex_LiteratureDb bibtex_literaturedb;




    private List<Bibtex_Author> bibtex_authors;




    private Bibtex_LiteratureDb bibtex_literaturedb;


    public Bibtex_Entry(
        String id,        String title    ) {
        this.id = id;
        this.title = title;
        this.bibtex_authors = new ArrayList<>();
    }

    public Bibtex_Entry(
        String id,        String title        ArrayList<Bibtex_Author> bibtex_authors    ) {
        this.id = id;
        this.title = title;
        this.bibtex_authors = bibtex_authors;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public Bibtex_Author getBibtex_author() {
        return bibtex_author;
    }

    public void setBibtex_author(Bibtex_Author bibtex_author) {
        this.bibtex_author = bibtex_author;
    }
    public Bibtex_LiteratureDb getBibtex_literaturedb() {
        return bibtex_literaturedb;
    }

    public void setBibtex_literaturedb(Bibtex_LiteratureDb bibtex_literaturedb) {
        this.bibtex_literaturedb = bibtex_literaturedb;
    }
    public List<Bibtex_Author> getBibtex_authors() {
        return bibtex_authors;
    }

    public void addBibtex_author(Bibtex_author bibtex_author) {
        this.bibtex_authors.add(bibtex_author);
    }
    public Bibtex_LiteratureDb getBibtex_literaturedb() {
        return bibtex_literaturedb;
    }

    public void setBibtex_literaturedb(Bibtex_LiteratureDb bibtex_literaturedb) {
        this.bibtex_literaturedb = bibtex_literaturedb;
    }

}