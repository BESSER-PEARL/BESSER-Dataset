





import java.util.List;
import java.util.ArrayList;

public class sadl_TypedBNode  {

    private String article;





    private sadl_NecessaryAndSufficient sadl_necessaryandsufficient;




    private sadl_ResourceIdentifier sadl_resourceidentifier;


    public sadl_TypedBNode(
        String article    ) {
        this.article = article;
    }


    public String getArticle() {
        return article;
    }

    public void setArticle(String article) {
        this.article = article;
    }

    public sadl_NecessaryAndSufficient getSadl_necessaryandsufficient() {
        return sadl_necessaryandsufficient;
    }

    public void setSadl_necessaryandsufficient(sadl_NecessaryAndSufficient sadl_necessaryandsufficient) {
        this.sadl_necessaryandsufficient = sadl_necessaryandsufficient;
    }
    public sadl_ResourceIdentifier getSadl_resourceidentifier() {
        return sadl_resourceidentifier;
    }

    public void setSadl_resourceidentifier(sadl_ResourceIdentifier sadl_resourceidentifier) {
        this.sadl_resourceidentifier = sadl_resourceidentifier;
    }

}