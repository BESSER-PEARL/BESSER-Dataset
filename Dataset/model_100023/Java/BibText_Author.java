





import java.util.List;
import java.util.ArrayList;

public class BibText_Author extends BibTextEntry {

    private String name;





    private BibText_Article bibtext_article;




    private List<BibText_Article> bibtext_articles;


    public BibText_Author(
        String name    ) {
        super(
        );
        this.name = name;
        this.bibtext_articles = new ArrayList<>();
    }

    public BibText_Author(
        String name        ArrayList<BibText_Article> bibtext_articles    ) {
        this.name = name;
        this.bibtext_articles = bibtext_articles;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public BibText_Article getBibtext_article() {
        return bibtext_article;
    }

    public void setBibtext_article(BibText_Article bibtext_article) {
        this.bibtext_article = bibtext_article;
    }
    public List<BibText_Article> getBibtext_articles() {
        return bibtext_articles;
    }

    public void addBibtext_article(Bibtext_article bibtext_article) {
        this.bibtext_articles.add(bibtext_article);
    }

}