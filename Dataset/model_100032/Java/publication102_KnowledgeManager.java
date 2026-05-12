





import java.util.List;
import java.util.ArrayList;

public class publication102_KnowledgeManager extends Named {






    private List<publication102_Keyword> publication102_keywords;


    public publication102_KnowledgeManager(
    ) {
        super(
        );
        this.publication102_keywords = new ArrayList<>();
    }

    public publication102_KnowledgeManager(
        ArrayList<publication102_Keyword> publication102_keywords    ) {
        this.publication102_keywords = publication102_keywords;
    }


    public List<publication102_Keyword> getPublication102_keywords() {
        return publication102_keywords;
    }

    public void addPublication102_keyword(Publication102_keyword publication102_keyword) {
        this.publication102_keywords.add(publication102_keyword);
    }

}