





import java.util.List;
import java.util.ArrayList;

public class research_Keyword extends Named {

    private String description;





    private List<research_Paper> research_papers;


    public research_Keyword(
        String description    ) {
        super(
        );
        this.description = description;
        this.research_papers = new ArrayList<>();
    }

    public research_Keyword(
        String description        ArrayList<research_Paper> research_papers    ) {
        this.description = description;
        this.research_papers = research_papers;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<research_Paper> getResearch_papers() {
        return research_papers;
    }

    public void addResearch_paper(Research_paper research_paper) {
        this.research_papers.add(research_paper);
    }

}