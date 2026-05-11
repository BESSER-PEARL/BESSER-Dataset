





import java.util.List;
import java.util.ArrayList;

public class sadl_InstanceDeclaration extends InstanceDeclarationStatement, EmbeddedInstanceDeclaration {

    private String article;





    private sadl_ResourceByName sadl_resourcebyname;




    private sadl_PropValPartialTriple sadl_propvalpartialtriple;




    private sadl_ResourceName sadl_resourcename;




    private List<sadl_PropValPartialTriple> sadl_propvalpartialtriples;


    public sadl_InstanceDeclaration(
        String article    ) {
        super(
        );
        this.article = article;
        this.sadl_propvalpartialtriples = new ArrayList<>();
    }

    public sadl_InstanceDeclaration(
        String article        ArrayList<sadl_PropValPartialTriple> sadl_propvalpartialtriples    ) {
        this.article = article;
        this.sadl_propvalpartialtriples = sadl_propvalpartialtriples;
    }

    public String getArticle() {
        return article;
    }

    public void setArticle(String article) {
        this.article = article;
    }

    public sadl_ResourceByName getSadl_resourcebyname() {
        return sadl_resourcebyname;
    }

    public void setSadl_resourcebyname(sadl_ResourceByName sadl_resourcebyname) {
        this.sadl_resourcebyname = sadl_resourcebyname;
    }
    public sadl_PropValPartialTriple getSadl_propvalpartialtriple() {
        return sadl_propvalpartialtriple;
    }

    public void setSadl_propvalpartialtriple(sadl_PropValPartialTriple sadl_propvalpartialtriple) {
        this.sadl_propvalpartialtriple = sadl_propvalpartialtriple;
    }
    public sadl_ResourceName getSadl_resourcename() {
        return sadl_resourcename;
    }

    public void setSadl_resourcename(sadl_ResourceName sadl_resourcename) {
        this.sadl_resourcename = sadl_resourcename;
    }
    public List<sadl_PropValPartialTriple> getSadl_propvalpartialtriples() {
        return sadl_propvalpartialtriples;
    }

    public void addSadl_propvalpartialtriple(Sadl_propvalpartialtriple sadl_propvalpartialtriple) {
        this.sadl_propvalpartialtriples.add(sadl_propvalpartialtriple);
    }

}