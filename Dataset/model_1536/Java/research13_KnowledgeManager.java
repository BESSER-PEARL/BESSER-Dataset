





import java.util.List;
import java.util.ArrayList;

public class research13_KnowledgeManager extends Named {






    private List<research13_Keyword> research13_keywords;


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

}