





import java.util.List;
import java.util.ArrayList;

public class research_KnowledgeManager extends Named {






    private List<research_Keyword> research_keywords;


    public research_KnowledgeManager(
    ) {
        super(
        );
        this.research_keywords = new ArrayList<>();
    }

    public research_KnowledgeManager(
        ArrayList<research_Keyword> research_keywords    ) {
        this.research_keywords = research_keywords;
    }


    public List<research_Keyword> getResearch_keywords() {
        return research_keywords;
    }

    public void addResearch_keyword(Research_keyword research_keyword) {
        this.research_keywords.add(research_keyword);
    }

}