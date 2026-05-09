





import java.util.List;
import java.util.ArrayList;

public class research20_PublicationSystem extends Named {






    private research20_PublicationProcess research20_publicationprocess;




    private List<research20_Position> research20_positions;




    private research20_PublicationStructure research20_publicationstructure;


    public research20_PublicationSystem(
    ) {
        super(
        );
        this.research20_positions = new ArrayList<>();
    }

    public research20_PublicationSystem(
        ArrayList<research20_Position> research20_positions    ) {
        this.research20_positions = research20_positions;
    }


    public research20_PublicationProcess getResearch20_publicationprocess() {
        return research20_publicationprocess;
    }

    public void setResearch20_publicationprocess(research20_PublicationProcess research20_publicationprocess) {
        this.research20_publicationprocess = research20_publicationprocess;
    }
    public List<research20_Position> getResearch20_positions() {
        return research20_positions;
    }

    public void addResearch20_position(Research20_position research20_position) {
        this.research20_positions.add(research20_position);
    }
    public research20_PublicationStructure getResearch20_publicationstructure() {
        return research20_publicationstructure;
    }

    public void setResearch20_publicationstructure(research20_PublicationStructure research20_publicationstructure) {
        this.research20_publicationstructure = research20_publicationstructure;
    }

}