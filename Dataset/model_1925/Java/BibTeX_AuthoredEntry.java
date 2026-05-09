





import java.util.List;
import java.util.ArrayList;

public class BibTeX_AuthoredEntry extends BibTeXEntry {






    private List<BibTeX_Author> bibtex_authors;


    public BibTeX_AuthoredEntry(
    ) {
        super(
        );
        this.bibtex_authors = new ArrayList<>();
    }

    public BibTeX_AuthoredEntry(
        ArrayList<BibTeX_Author> bibtex_authors    ) {
        this.bibtex_authors = bibtex_authors;
    }


    public List<BibTeX_Author> getBibtex_authors() {
        return bibtex_authors;
    }

    public void addBibtex_author(Bibtex_author bibtex_author) {
        this.bibtex_authors.add(bibtex_author);
    }

}