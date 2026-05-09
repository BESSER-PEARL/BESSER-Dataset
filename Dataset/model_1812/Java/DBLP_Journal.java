





import java.util.List;
import java.util.ArrayList;

public class DBLP_Journal  {

    private String name;





    private List<DBLP_Article> dblp_articles;




    private DBLP_Article dblp_article;


    public DBLP_Journal(
        String name    ) {
        this.name = name;
        this.dblp_articles = new ArrayList<>();
    }

    public DBLP_Journal(
        String name        ArrayList<DBLP_Article> dblp_articles    ) {
        this.name = name;
        this.dblp_articles = dblp_articles;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<DBLP_Article> getDblp_articles() {
        return dblp_articles;
    }

    public void addDblp_article(Dblp_article dblp_article) {
        this.dblp_articles.add(dblp_article);
    }
    public DBLP_Article getDblp_article() {
        return dblp_article;
    }

    public void setDblp_article(DBLP_Article dblp_article) {
        this.dblp_article = dblp_article;
    }

}