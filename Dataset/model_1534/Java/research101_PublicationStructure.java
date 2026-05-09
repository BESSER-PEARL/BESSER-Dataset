





import java.util.List;
import java.util.ArrayList;

public class research101_PublicationStructure extends Named {






    private List<research101_Paper> research101_papers;


    public research101_PublicationStructure(
    ) {
        super(
        );
        this.research101_papers = new ArrayList<>();
    }

    public research101_PublicationStructure(
        ArrayList<research101_Paper> research101_papers    ) {
        this.research101_papers = research101_papers;
    }


    public List<research101_Paper> getResearch101_papers() {
        return research101_papers;
    }

    public void addResearch101_paper(Research101_paper research101_paper) {
        this.research101_papers.add(research101_paper);
    }

}