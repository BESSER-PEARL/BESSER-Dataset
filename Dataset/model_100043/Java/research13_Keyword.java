





import java.util.List;
import java.util.ArrayList;

public class research13_Keyword extends Named {

    private String description;





    private List<research13_Paper> research13_papers;


    public research13_Keyword(
        String description    ) {
        super(
        );
        this.description = description;
        this.research13_papers = new ArrayList<>();
    }

    public research13_Keyword(
        String description        ArrayList<research13_Paper> research13_papers    ) {
        this.description = description;
        this.research13_papers = research13_papers;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<research13_Paper> getResearch13_papers() {
        return research13_papers;
    }

    public void addResearch13_paper(Research13_paper research13_paper) {
        this.research13_papers.add(research13_paper);
    }

}