





import java.util.List;
import java.util.ArrayList;

public class research101_PublicationSystem extends Named {






    private List<research101_Position> research101_positions;




    private research101_PublicationProcess research101_publicationprocess;




    private research101_PublicationStructure research101_publicationstructure;


    public research101_PublicationSystem(
    ) {
        super(
        );
        this.research101_positions = new ArrayList<>();
    }

    public research101_PublicationSystem(
        ArrayList<research101_Position> research101_positions    ) {
        this.research101_positions = research101_positions;
    }


    public List<research101_Position> getResearch101_positions() {
        return research101_positions;
    }

    public void addResearch101_position(Research101_position research101_position) {
        this.research101_positions.add(research101_position);
    }
    public research101_PublicationProcess getResearch101_publicationprocess() {
        return research101_publicationprocess;
    }

    public void setResearch101_publicationprocess(research101_PublicationProcess research101_publicationprocess) {
        this.research101_publicationprocess = research101_publicationprocess;
    }
    public research101_PublicationStructure getResearch101_publicationstructure() {
        return research101_publicationstructure;
    }

    public void setResearch101_publicationstructure(research101_PublicationStructure research101_publicationstructure) {
        this.research101_publicationstructure = research101_publicationstructure;
    }

}