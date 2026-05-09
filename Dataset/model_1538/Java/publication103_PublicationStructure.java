





import java.util.List;
import java.util.ArrayList;

public class publication103_PublicationStructure extends Named {






    private List<publication103_Position> publication103_positions;




    private List<publication103_Paper> publication103_papers;


    public publication103_PublicationStructure(
    ) {
        super(
        );
        this.publication103_positions = new ArrayList<>();
        this.publication103_papers = new ArrayList<>();
    }

    public publication103_PublicationStructure(
        ArrayList<publication103_Position> publication103_positions,        ArrayList<publication103_Paper> publication103_papers    ) {
        this.publication103_positions = publication103_positions;
        this.publication103_papers = publication103_papers;
    }


    public List<publication103_Position> getPublication103_positions() {
        return publication103_positions;
    }

    public void addPublication103_position(Publication103_position publication103_position) {
        this.publication103_positions.add(publication103_position);
    }
    public List<publication103_Paper> getPublication103_papers() {
        return publication103_papers;
    }

    public void addPublication103_paper(Publication103_paper publication103_paper) {
        this.publication103_papers.add(publication103_paper);
    }

}