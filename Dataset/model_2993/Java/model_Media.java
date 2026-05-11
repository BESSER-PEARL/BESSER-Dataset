





import java.util.List;
import java.util.ArrayList;

public class model_Media extends Content {

    private String typePrefix;





    private List<model_Article> model_articles;


    public model_Media(
        String typePrefix    ) {
        super(
        );
        this.typePrefix = typePrefix;
        this.model_articles = new ArrayList<>();
    }

    public model_Media(
        String typePrefix        ArrayList<model_Article> model_articles    ) {
        this.typePrefix = typePrefix;
        this.model_articles = model_articles;
    }

    public String getTypeprefix() {
        return typePrefix;
    }

    public void setTypeprefix(String typePrefix) {
        this.typePrefix = typePrefix;
    }

    public List<model_Article> getModel_articles() {
        return model_articles;
    }

    public void addModel_article(Model_article model_article) {
        this.model_articles.add(model_article);
    }

}