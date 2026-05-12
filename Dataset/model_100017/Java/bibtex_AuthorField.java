





import java.util.List;
import java.util.ArrayList;

public class bibtex_AuthorField extends Field {






    private List<bibtex_Author> bibtex_authors;


    public bibtex_AuthorField(
    ) {
        super(
        );
        this.bibtex_authors = new ArrayList<>();
    }

    public bibtex_AuthorField(
        ArrayList<bibtex_Author> bibtex_authors    ) {
        this.bibtex_authors = bibtex_authors;
    }


    public List<bibtex_Author> getBibtex_authors() {
        return bibtex_authors;
    }

    public void addBibtex_author(Bibtex_author bibtex_author) {
        this.bibtex_authors.add(bibtex_author);
    }

}