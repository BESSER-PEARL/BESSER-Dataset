





import java.util.List;
import java.util.ArrayList;

public class publication102_PublicationStructure extends Named {






    private List<publication102_Paper> publication102_papers;




    private List<publication102_Researcher> publication102_researchers;




    private List<publication102_Position> publication102_positions;


    public publication102_PublicationStructure(
    ) {
        super(
        );
        this.publication102_papers = new ArrayList<>();
        this.publication102_researchers = new ArrayList<>();
        this.publication102_positions = new ArrayList<>();
    }

    public publication102_PublicationStructure(
        ArrayList<publication102_Paper> publication102_papers,        ArrayList<publication102_Researcher> publication102_researchers,        ArrayList<publication102_Position> publication102_positions    ) {
        this.publication102_papers = publication102_papers;
        this.publication102_researchers = publication102_researchers;
        this.publication102_positions = publication102_positions;
    }


    public List<publication102_Paper> getPublication102_papers() {
        return publication102_papers;
    }

    public void addPublication102_paper(Publication102_paper publication102_paper) {
        this.publication102_papers.add(publication102_paper);
    }
    public List<publication102_Researcher> getPublication102_researchers() {
        return publication102_researchers;
    }

    public void addPublication102_researcher(Publication102_researcher publication102_researcher) {
        this.publication102_researchers.add(publication102_researcher);
    }
    public List<publication102_Position> getPublication102_positions() {
        return publication102_positions;
    }

    public void addPublication102_position(Publication102_position publication102_position) {
        this.publication102_positions.add(publication102_position);
    }

}