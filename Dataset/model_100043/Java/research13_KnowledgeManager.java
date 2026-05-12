





import java.util.List;
import java.util.ArrayList;

public class research13_KnowledgeManager extends Named {






    private List<research13_Keyword> research13_keywords;




    private research13_PublicationStructure research13_publicationstructure;


    public research13_KnowledgeManager(
    ) {
        super(
        );
        this.research13_keywords = new ArrayList<>();
    }

    public research13_KnowledgeManager(
        ArrayList<research13_Keyword> research13_keywords    ) {
        this.research13_keywords = research13_keywords;
    }


    public List<research13_Keyword> getResearch13_keywords() {
        return research13_keywords;
    }

    public void addResearch13_keyword(Research13_keyword research13_keyword) {
        this.research13_keywords.add(research13_keyword);
    }
    public research13_PublicationStructure getResearch13_publicationstructure() {
        return research13_publicationstructure;
    }

    public void setResearch13_publicationstructure(research13_PublicationStructure research13_publicationstructure) {
        this.research13_publicationstructure = research13_publicationstructure;
    }

}