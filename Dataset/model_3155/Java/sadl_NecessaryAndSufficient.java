





import java.util.List;
import java.util.ArrayList;

public class sadl_NecessaryAndSufficient extends Statement {

    private String article;





    private sadl_ResourceName sadl_resourcename;




    private List<sadl_Condition> sadl_conditions;




    private List<sadl_ResourceByName> sadl_resourcebynames;


    public sadl_NecessaryAndSufficient(
        String article    ) {
        super(
        );
        this.article = article;
        this.sadl_conditions = new ArrayList<>();
        this.sadl_resourcebynames = new ArrayList<>();
    }

    public sadl_NecessaryAndSufficient(
        String article        ArrayList<sadl_Condition> sadl_conditions,        ArrayList<sadl_ResourceByName> sadl_resourcebynames    ) {
        this.article = article;
        this.sadl_conditions = sadl_conditions;
        this.sadl_resourcebynames = sadl_resourcebynames;
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
    public List<sadl_Condition> getSadl_conditions() {
        return sadl_conditions;
    }

    public void addSadl_condition(Sadl_condition sadl_condition) {
        this.sadl_conditions.add(sadl_condition);
    }
    public List<sadl_ResourceByName> getSadl_resourcebynames() {
        return sadl_resourcebynames;
    }

    public void addSadl_resourcebyname(Sadl_resourcebyname sadl_resourcebyname) {
        this.sadl_resourcebynames.add(sadl_resourcebyname);
    }

}