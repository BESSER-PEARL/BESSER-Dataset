





import java.util.List;
import java.util.ArrayList;

public class research23_PublicationSystem extends Named {






    private research23_PublicationProcess research23_publicationprocess;




    private List<research23_Position> research23_positions;




    private research23_PublicationStructure research23_publicationstructure;


    public research23_PublicationSystem(
    ) {
        super(
        );
        this.research23_positions = new ArrayList<>();
    }

    public research23_PublicationSystem(
        ArrayList<research23_Position> research23_positions    ) {
        this.research23_positions = research23_positions;
    }


    public research23_PublicationProcess getResearch23_publicationprocess() {
        return research23_publicationprocess;
    }

    public void setResearch23_publicationprocess(research23_PublicationProcess research23_publicationprocess) {
        this.research23_publicationprocess = research23_publicationprocess;
    }
    public List<research23_Position> getResearch23_positions() {
        return research23_positions;
    }

    public void addResearch23_position(Research23_position research23_position) {
        this.research23_positions.add(research23_position);
    }
    public research23_PublicationStructure getResearch23_publicationstructure() {
        return research23_publicationstructure;
    }

    public void setResearch23_publicationstructure(research23_PublicationStructure research23_publicationstructure) {
        this.research23_publicationstructure = research23_publicationstructure;
    }

}