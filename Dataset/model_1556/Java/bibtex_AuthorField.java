





import java.util.List;
import java.util.ArrayList;

public class bibtex_AuthorField extends Field {






    private List<bibtex_Author> bibtex_authors;




    private bibtex_InProceedingsEntry bibtex_inproceedingsentry;




    private bibtex_ArticleEntry bibtex_articleentry;


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
    public bibtex_InProceedingsEntry getBibtex_inproceedingsentry() {
        return bibtex_inproceedingsentry;
    }

    public void setBibtex_inproceedingsentry(bibtex_InProceedingsEntry bibtex_inproceedingsentry) {
        this.bibtex_inproceedingsentry = bibtex_inproceedingsentry;
    }
    public bibtex_ArticleEntry getBibtex_articleentry() {
        return bibtex_articleentry;
    }

    public void setBibtex_articleentry(bibtex_ArticleEntry bibtex_articleentry) {
        this.bibtex_articleentry = bibtex_articleentry;
    }

}