





import java.util.List;
import java.util.ArrayList;

public class sourceanalysator_Library  {






    private List<sourceanalysator_Hyperlink> sourceanalysator_hyperlinks;




    private List<sourceanalysator_Article> sourceanalysator_articles;




    private List<sourceanalysator_GeneralSource> sourceanalysator_generalsources;


    public sourceanalysator_Library(
    ) {
        this.sourceanalysator_hyperlinks = new ArrayList<>();
        this.sourceanalysator_articles = new ArrayList<>();
        this.sourceanalysator_generalsources = new ArrayList<>();
    }

    public sourceanalysator_Library(
        ArrayList<sourceanalysator_Hyperlink> sourceanalysator_hyperlinks,        ArrayList<sourceanalysator_Article> sourceanalysator_articles,        ArrayList<sourceanalysator_GeneralSource> sourceanalysator_generalsources    ) {
        this.sourceanalysator_hyperlinks = sourceanalysator_hyperlinks;
        this.sourceanalysator_articles = sourceanalysator_articles;
        this.sourceanalysator_generalsources = sourceanalysator_generalsources;
    }


    public List<sourceanalysator_Hyperlink> getSourceanalysator_hyperlinks() {
        return sourceanalysator_hyperlinks;
    }

    public void addSourceanalysator_hyperlink(Sourceanalysator_hyperlink sourceanalysator_hyperlink) {
        this.sourceanalysator_hyperlinks.add(sourceanalysator_hyperlink);
    }
    public List<sourceanalysator_Article> getSourceanalysator_articles() {
        return sourceanalysator_articles;
    }

    public void addSourceanalysator_article(Sourceanalysator_article sourceanalysator_article) {
        this.sourceanalysator_articles.add(sourceanalysator_article);
    }
    public List<sourceanalysator_GeneralSource> getSourceanalysator_generalsources() {
        return sourceanalysator_generalsources;
    }

    public void addSourceanalysator_generalsource(Sourceanalysator_generalsource sourceanalysator_generalsource) {
        this.sourceanalysator_generalsources.add(sourceanalysator_generalsource);
    }

}