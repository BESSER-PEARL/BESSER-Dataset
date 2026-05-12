





import java.util.List;
import java.util.ArrayList;

public class bibtex_Journal  {

    private String journal;





    private bibtex_Article bibtex_article;


    public bibtex_Journal(
        String journal    ) {
        this.journal = journal;
    }


    public String getJournal() {
        return journal;
    }

    public void setJournal(String journal) {
        this.journal = journal;
    }

    public bibtex_Article getBibtex_article() {
        return bibtex_article;
    }

    public void setBibtex_article(bibtex_Article bibtex_article) {
        this.bibtex_article = bibtex_article;
    }

}