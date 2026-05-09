





import java.util.List;
import java.util.ArrayList;

public class tp6_KnowledgeManager  {

    private String name;





    private List<tp6_Keyword> tp6_keywords;




    private tp6_PublicationStructure tp6_publicationstructure;


    public tp6_KnowledgeManager(
        String name    ) {
        this.name = name;
        this.tp6_keywords = new ArrayList<>();
    }

    public tp6_KnowledgeManager(
        String name        ArrayList<tp6_Keyword> tp6_keywords    ) {
        this.name = name;
        this.tp6_keywords = tp6_keywords;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<tp6_Keyword> getTp6_keywords() {
        return tp6_keywords;
    }

    public void addTp6_keyword(Tp6_keyword tp6_keyword) {
        this.tp6_keywords.add(tp6_keyword);
    }
    public tp6_PublicationStructure getTp6_publicationstructure() {
        return tp6_publicationstructure;
    }

    public void setTp6_publicationstructure(tp6_PublicationStructure tp6_publicationstructure) {
        this.tp6_publicationstructure = tp6_publicationstructure;
    }

}