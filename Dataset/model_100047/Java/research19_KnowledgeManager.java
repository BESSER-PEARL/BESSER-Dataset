





import java.util.List;
import java.util.ArrayList;

public class research19_KnowledgeManager extends Named {






    private List<research19_Keyword> research19_keywords;


    public research19_KnowledgeManager(
    ) {
        super(
        );
        this.research19_keywords = new ArrayList<>();
    }

    public research19_KnowledgeManager(
        ArrayList<research19_Keyword> research19_keywords    ) {
        this.research19_keywords = research19_keywords;
    }


    public List<research19_Keyword> getResearch19_keywords() {
        return research19_keywords;
    }

    public void addResearch19_keyword(Research19_keyword research19_keyword) {
        this.research19_keywords.add(research19_keyword);
    }

}