





import java.util.List;
import java.util.ArrayList;

public class article_Documentation extends StructuralElement {

    private String project;





    private article_Documentation article_documentation;


    public article_Documentation(
        String project    ) {
        super(
        );
        this.project = project;
    }


    public String getProject() {
        return project;
    }

    public void setProject(String project) {
        this.project = project;
    }

    public article_Documentation getArticle_documentation() {
        return article_documentation;
    }

    public void setArticle_documentation(article_Documentation article_documentation) {
        this.article_documentation = article_documentation;
    }

}