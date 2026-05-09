





import java.util.List;
import java.util.ArrayList;

public class bibTeX_AuthoredEntry extends BibTeXEntry {






    private List<bibTeX_Author> bibtex_authors;


    public bibTeX_AuthoredEntry(
    ) {
        super(
        );
        this.bibtex_authors = new ArrayList<>();
    }

    public bibTeX_AuthoredEntry(
        ArrayList<bibTeX_Author> bibtex_authors    ) {
        this.bibtex_authors = bibtex_authors;
    }


    public List<bibTeX_Author> getBibtex_authors() {
        return bibtex_authors;
    }

    public void addBibtex_author(Bibtex_author bibtex_author) {
        this.bibtex_authors.add(bibtex_author);
    }

}