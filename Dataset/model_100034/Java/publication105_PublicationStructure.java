





import java.util.List;
import java.util.ArrayList;

public class publication105_PublicationStructure extends Named {






    private List<publication105_Position> publication105_positions;




    private List<publication105_Researcher> publication105_researchers;




    private List<publication105_Paper> publication105_papers;


    public publication105_PublicationStructure(
    ) {
        super(
        );
        this.publication105_positions = new ArrayList<>();
        this.publication105_researchers = new ArrayList<>();
        this.publication105_papers = new ArrayList<>();
    }

    public publication105_PublicationStructure(
        ArrayList<publication105_Position> publication105_positions,        ArrayList<publication105_Researcher> publication105_researchers,        ArrayList<publication105_Paper> publication105_papers    ) {
        this.publication105_positions = publication105_positions;
        this.publication105_researchers = publication105_researchers;
        this.publication105_papers = publication105_papers;
    }


    public List<publication105_Position> getPublication105_positions() {
        return publication105_positions;
    }

    public void addPublication105_position(Publication105_position publication105_position) {
        this.publication105_positions.add(publication105_position);
    }
    public List<publication105_Researcher> getPublication105_researchers() {
        return publication105_researchers;
    }

    public void addPublication105_researcher(Publication105_researcher publication105_researcher) {
        this.publication105_researchers.add(publication105_researcher);
    }
    public List<publication105_Paper> getPublication105_papers() {
        return publication105_papers;
    }

    public void addPublication105_paper(Publication105_paper publication105_paper) {
        this.publication105_papers.add(publication105_paper);
    }

}