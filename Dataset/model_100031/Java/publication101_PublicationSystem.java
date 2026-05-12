





import java.util.List;
import java.util.ArrayList;

public class publication101_PublicationSystem extends Named {






    private List<publication101_Position> publication101_positions;




    private publication101_PublicationStructure publication101_publicationstructure;




    private publication101_PublicationProcess publication101_publicationprocess;


    public publication101_PublicationSystem(
    ) {
        super(
        );
        this.publication101_positions = new ArrayList<>();
    }

    public publication101_PublicationSystem(
        ArrayList<publication101_Position> publication101_positions    ) {
        this.publication101_positions = publication101_positions;
    }


    public List<publication101_Position> getPublication101_positions() {
        return publication101_positions;
    }

    public void addPublication101_position(Publication101_position publication101_position) {
        this.publication101_positions.add(publication101_position);
    }
    public publication101_PublicationStructure getPublication101_publicationstructure() {
        return publication101_publicationstructure;
    }

    public void setPublication101_publicationstructure(publication101_PublicationStructure publication101_publicationstructure) {
        this.publication101_publicationstructure = publication101_publicationstructure;
    }
    public publication101_PublicationProcess getPublication101_publicationprocess() {
        return publication101_publicationprocess;
    }

    public void setPublication101_publicationprocess(publication101_PublicationProcess publication101_publicationprocess) {
        this.publication101_publicationprocess = publication101_publicationprocess;
    }

}