





import java.util.List;
import java.util.ArrayList;

public class article_Context  {

    private String baseFolder;
    private String project;
    private String root;





    private List<article_Documentation> article_documentations;




    private article_Documentation article_documentation;


    public article_Context(
        String baseFolder,        String project,        String root    ) {
        this.baseFolder = baseFolder;
        this.project = project;
        this.root = root;
        this.article_documentations = new ArrayList<>();
    }

    public article_Context(
        String baseFolder,        String project,        String root        ArrayList<article_Documentation> article_documentations    ) {
        this.baseFolder = baseFolder;
        this.project = project;
        this.root = root;
        this.article_documentations = article_documentations;
    }

    public String getBasefolder() {
        return baseFolder;
    }

    public void setBasefolder(String baseFolder) {
        this.baseFolder = baseFolder;
    }
    public String getProject() {
        return project;
    }

    public void setProject(String project) {
        this.project = project;
    }
    public String getRoot() {
        return root;
    }

    public void setRoot(String root) {
        this.root = root;
    }

    public List<article_Documentation> getArticle_documentations() {
        return article_documentations;
    }

    public void addArticle_documentation(Article_documentation article_documentation) {
        this.article_documentations.add(article_documentation);
    }
    public article_Documentation getArticle_documentation() {
        return article_documentation;
    }

    public void setArticle_documentation(article_Documentation article_documentation) {
        this.article_documentation = article_documentation;
    }

}