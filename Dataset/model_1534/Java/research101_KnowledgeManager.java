





import java.util.List;
import java.util.ArrayList;

public class research101_KnowledgeManager extends Named {






    private List<research101_Keyword> research101_keywords;




    private research101_PublicationStructure research101_publicationstructure;


    public research101_KnowledgeManager(
    ) {
        super(
        );
        this.research101_keywords = new ArrayList<>();
    }

    public research101_KnowledgeManager(
        ArrayList<research101_Keyword> research101_keywords    ) {
        this.research101_keywords = research101_keywords;
    }


    public List<research101_Keyword> getResearch101_keywords() {
        return research101_keywords;
    }

    public void addResearch101_keyword(Research101_keyword research101_keyword) {
        this.research101_keywords.add(research101_keyword);
    }
    public research101_PublicationStructure getResearch101_publicationstructure() {
        return research101_publicationstructure;
    }

    public void setResearch101_publicationstructure(research101_PublicationStructure research101_publicationstructure) {
        this.research101_publicationstructure = research101_publicationstructure;
    }

}