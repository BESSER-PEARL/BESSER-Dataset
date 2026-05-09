





import java.util.List;
import java.util.ArrayList;

public class research2_KnowledgeManager extends Named {






    private List<research2_Keyword> research2_keywords;




    private research2_PublicationStructure research2_publicationstructure;


    public research2_KnowledgeManager(
    ) {
        super(
        );
        this.research2_keywords = new ArrayList<>();
    }

    public research2_KnowledgeManager(
        ArrayList<research2_Keyword> research2_keywords    ) {
        this.research2_keywords = research2_keywords;
    }


    public List<research2_Keyword> getResearch2_keywords() {
        return research2_keywords;
    }

    public void addResearch2_keyword(Research2_keyword research2_keyword) {
        this.research2_keywords.add(research2_keyword);
    }
    public research2_PublicationStructure getResearch2_publicationstructure() {
        return research2_publicationstructure;
    }

    public void setResearch2_publicationstructure(research2_PublicationStructure research2_publicationstructure) {
        this.research2_publicationstructure = research2_publicationstructure;
    }

}