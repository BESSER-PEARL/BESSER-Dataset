





import java.util.List;
import java.util.ArrayList;

public class bibTeX_PagesField  {

    private String pages;





    private bibTeX_Article bibtex_article;


    public bibTeX_PagesField(
        String pages    ) {
        this.pages = pages;
    }


    public String getPages() {
        return pages;
    }

    public void setPages(String pages) {
        this.pages = pages;
    }

    public bibTeX_Article getBibtex_article() {
        return bibtex_article;
    }

    public void setBibtex_article(bibTeX_Article bibtex_article) {
        this.bibtex_article = bibtex_article;
    }

}