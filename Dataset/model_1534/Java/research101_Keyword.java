





import java.util.List;
import java.util.ArrayList;

public class research101_Keyword extends Named {

    private String description;





    private List<research101_Paper> research101_papers;


    public research101_Keyword(
        String description    ) {
        super(
        );
        this.description = description;
        this.research101_papers = new ArrayList<>();
    }

    public research101_Keyword(
        String description        ArrayList<research101_Paper> research101_papers    ) {
        this.description = description;
        this.research101_papers = research101_papers;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<research101_Paper> getResearch101_papers() {
        return research101_papers;
    }

    public void addResearch101_paper(Research101_paper research101_paper) {
        this.research101_papers.add(research101_paper);
    }

}