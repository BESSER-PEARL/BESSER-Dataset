





import java.util.List;
import java.util.ArrayList;

public class research31_KnowledgeManager extends Named {






    private List<research31_Keyword> research31_keywords;




    private research31_PublicationStructure research31_publicationstructure;


    public research31_KnowledgeManager(
    ) {
        super(
        );
        this.research31_keywords = new ArrayList<>();
    }

    public research31_KnowledgeManager(
        ArrayList<research31_Keyword> research31_keywords    ) {
        this.research31_keywords = research31_keywords;
    }


    public List<research31_Keyword> getResearch31_keywords() {
        return research31_keywords;
    }

    public void addResearch31_keyword(Research31_keyword research31_keyword) {
        this.research31_keywords.add(research31_keyword);
    }
    public research31_PublicationStructure getResearch31_publicationstructure() {
        return research31_publicationstructure;
    }

    public void setResearch31_publicationstructure(research31_PublicationStructure research31_publicationstructure) {
        this.research31_publicationstructure = research31_publicationstructure;
    }

}