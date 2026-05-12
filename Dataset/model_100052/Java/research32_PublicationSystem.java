





import java.util.List;
import java.util.ArrayList;

public class research32_PublicationSystem extends Named {






    private List<research32_Position> research32_positions;




    private research32_PublicationStructure research32_publicationstructure;




    private research32_PublicationProcess research32_publicationprocess;


    public research32_PublicationSystem(
    ) {
        super(
        );
        this.research32_positions = new ArrayList<>();
    }

    public research32_PublicationSystem(
        ArrayList<research32_Position> research32_positions    ) {
        this.research32_positions = research32_positions;
    }


    public List<research32_Position> getResearch32_positions() {
        return research32_positions;
    }

    public void addResearch32_position(Research32_position research32_position) {
        this.research32_positions.add(research32_position);
    }
    public research32_PublicationStructure getResearch32_publicationstructure() {
        return research32_publicationstructure;
    }

    public void setResearch32_publicationstructure(research32_PublicationStructure research32_publicationstructure) {
        this.research32_publicationstructure = research32_publicationstructure;
    }
    public research32_PublicationProcess getResearch32_publicationprocess() {
        return research32_publicationprocess;
    }

    public void setResearch32_publicationprocess(research32_PublicationProcess research32_publicationprocess) {
        this.research32_publicationprocess = research32_publicationprocess;
    }

}