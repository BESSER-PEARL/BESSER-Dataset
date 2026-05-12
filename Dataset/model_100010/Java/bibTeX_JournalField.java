





import java.util.List;
import java.util.ArrayList;

public class bibTeX_JournalField  {

    private String journal;





    private bibTeX_Article bibtex_article;


    public bibTeX_JournalField(
        String journal    ) {
        this.journal = journal;
    }


    public String getJournal() {
        return journal;
    }

    public void setJournal(String journal) {
        this.journal = journal;
    }

    public bibTeX_Article getBibtex_article() {
        return bibtex_article;
    }

    public void setBibtex_article(bibTeX_Article bibtex_article) {
        this.bibtex_article = bibtex_article;
    }

}