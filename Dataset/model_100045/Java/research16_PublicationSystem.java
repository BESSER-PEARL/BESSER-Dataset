





import java.util.List;
import java.util.ArrayList;

public class research16_PublicationSystem extends Named {






    private research16_PublicationStructure research16_publicationstructure;




    private List<research16_Position> research16_positions;




    private research16_PublicationProcess research16_publicationprocess;


    public research16_PublicationSystem(
    ) {
        super(
        );
        this.research16_positions = new ArrayList<>();
    }

    public research16_PublicationSystem(
        ArrayList<research16_Position> research16_positions    ) {
        this.research16_positions = research16_positions;
    }


    public research16_PublicationStructure getResearch16_publicationstructure() {
        return research16_publicationstructure;
    }

    public void setResearch16_publicationstructure(research16_PublicationStructure research16_publicationstructure) {
        this.research16_publicationstructure = research16_publicationstructure;
    }
    public List<research16_Position> getResearch16_positions() {
        return research16_positions;
    }

    public void addResearch16_position(Research16_position research16_position) {
        this.research16_positions.add(research16_position);
    }
    public research16_PublicationProcess getResearch16_publicationprocess() {
        return research16_publicationprocess;
    }

    public void setResearch16_publicationprocess(research16_PublicationProcess research16_publicationprocess) {
        this.research16_publicationprocess = research16_publicationprocess;
    }

}