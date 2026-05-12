





import java.util.List;
import java.util.ArrayList;

public class research31_PublicationSystem extends Named {






    private List<research31_Position> research31_positions;




    private research31_PublicationStructure research31_publicationstructure;


    public research31_PublicationSystem(
    ) {
        super(
        );
        this.research31_positions = new ArrayList<>();
    }

    public research31_PublicationSystem(
        ArrayList<research31_Position> research31_positions    ) {
        this.research31_positions = research31_positions;
    }


    public List<research31_Position> getResearch31_positions() {
        return research31_positions;
    }

    public void addResearch31_position(Research31_position research31_position) {
        this.research31_positions.add(research31_position);
    }
    public research31_PublicationStructure getResearch31_publicationstructure() {
        return research31_publicationstructure;
    }

    public void setResearch31_publicationstructure(research31_PublicationStructure research31_publicationstructure) {
        this.research31_publicationstructure = research31_publicationstructure;
    }

}