





import java.util.List;
import java.util.ArrayList;

public class article_Plugin  {

    private String label;
    private String name;





    private article_Documentation article_documentation;


    public article_Plugin(
        String label,        String name    ) {
        this.label = label;
        this.name = name;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public article_Documentation getArticle_documentation() {
        return article_documentation;
    }

    public void setArticle_documentation(article_Documentation article_documentation) {
        this.article_documentation = article_documentation;
    }

}