





import java.util.List;
import java.util.ArrayList;

public class sadl_PropertyDeclaration extends Statement {

    private String article;





    private sadl_ResourceName sadl_resourcename;




    private sadl_ResourceByName sadl_resourcebyname;




    private sadl_ResourceName sadl_resourcename;




    private sadl_ResourceIdentifier sadl_resourceidentifier;




    private sadl_ResourceIdentifier sadl_resourceidentifier;


    public sadl_PropertyDeclaration(
        String article    ) {
        super(
        );
        this.article = article;
    }


    public String getArticle() {
        return article;
    }

    public void setArticle(String article) {
        this.article = article;
    }

    public sadl_ResourceName getSadl_resourcename() {
        return sadl_resourcename;
    }

    public void setSadl_resourcename(sadl_ResourceName sadl_resourcename) {
        this.sadl_resourcename = sadl_resourcename;
    }
    public sadl_ResourceByName getSadl_resourcebyname() {
        return sadl_resourcebyname;
    }

    public void setSadl_resourcebyname(sadl_ResourceByName sadl_resourcebyname) {
        this.sadl_resourcebyname = sadl_resourcebyname;
    }
    public sadl_ResourceName getSadl_resourcename() {
        return sadl_resourcename;
    }

    public void setSadl_resourcename(sadl_ResourceName sadl_resourcename) {
        this.sadl_resourcename = sadl_resourcename;
    }
    public sadl_ResourceIdentifier getSadl_resourceidentifier() {
        return sadl_resourceidentifier;
    }

    public void setSadl_resourceidentifier(sadl_ResourceIdentifier sadl_resourceidentifier) {
        this.sadl_resourceidentifier = sadl_resourceidentifier;
    }
    public sadl_ResourceIdentifier getSadl_resourceidentifier() {
        return sadl_resourceidentifier;
    }

    public void setSadl_resourceidentifier(sadl_ResourceIdentifier sadl_resourceidentifier) {
        this.sadl_resourceidentifier = sadl_resourceidentifier;
    }

}