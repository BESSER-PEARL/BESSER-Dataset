





import java.util.List;
import java.util.ArrayList;

public class article_StructuralElement extends LinkTarget {

    private String doc;
    private String title;





    private article_Documentation article_documentation;




    private article_StructuralElement article_structuralelement;




    private article_StructuralElement article_structuralelement;


    public article_StructuralElement(
        String doc,        String title    ) {
        super(
        );
        this.doc = doc;
        this.title = title;
    }


    public String getDoc() {
        return doc;
    }

    public void setDoc(String doc) {
        this.doc = doc;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public article_Documentation getArticle_documentation() {
        return article_documentation;
    }

    public void setArticle_documentation(article_Documentation article_documentation) {
        this.article_documentation = article_documentation;
    }
    public article_StructuralElement getArticle_structuralelement() {
        return article_structuralelement;
    }

    public void setArticle_structuralelement(article_StructuralElement article_structuralelement) {
        this.article_structuralelement = article_structuralelement;
    }
    public article_StructuralElement getArticle_structuralelement() {
        return article_structuralelement;
    }

    public void setArticle_structuralelement(article_StructuralElement article_structuralelement) {
        this.article_structuralelement = article_structuralelement;
    }

}