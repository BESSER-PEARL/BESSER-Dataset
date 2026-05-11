





import java.util.List;
import java.util.ArrayList;

public class article_TreeNode  {

    private String image;
    private String xmi_ID;
    private String label;





    private List<article_TreeNodeProperty> article_treenodepropertys;




    private List<article_TreeNode> article_treenodes;


    public article_TreeNode(
        String image,        String xmi_ID,        String label    ) {
        this.image = image;
        this.xmi_ID = xmi_ID;
        this.label = label;
        this.article_treenodepropertys = new ArrayList<>();
        this.article_treenodes = new ArrayList<>();
    }

    public article_TreeNode(
        String image,        String xmi_ID,        String label        ArrayList<article_TreeNodeProperty> article_treenodepropertys,        ArrayList<article_TreeNode> article_treenodes    ) {
        this.image = image;
        this.xmi_ID = xmi_ID;
        this.label = label;
        this.article_treenodepropertys = article_treenodepropertys;
        this.article_treenodes = article_treenodes;
    }

    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public String getXmi_id() {
        return xmi_ID;
    }

    public void setXmi_id(String xmi_ID) {
        this.xmi_ID = xmi_ID;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public List<article_TreeNodeProperty> getArticle_treenodepropertys() {
        return article_treenodepropertys;
    }

    public void addArticle_treenodeproperty(Article_treenodeproperty article_treenodeproperty) {
        this.article_treenodepropertys.add(article_treenodeproperty);
    }
    public List<article_TreeNode> getArticle_treenodes() {
        return article_treenodes;
    }

    public void addArticle_treenode(Article_treenode article_treenode) {
        this.article_treenodes.add(article_treenode);
    }

}