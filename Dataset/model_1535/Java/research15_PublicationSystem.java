





import java.util.List;
import java.util.ArrayList;

public class research15_PublicationSystem extends Named {






    private research15_PublicationProcess research15_publicationprocess;




    private List<research15_Position> research15_positions;


    public research15_PublicationSystem(
    ) {
        super(
        );
        this.research15_positions = new ArrayList<>();
    }

    public research15_PublicationSystem(
        ArrayList<research15_Position> research15_positions    ) {
        this.research15_positions = research15_positions;
    }


    public research15_PublicationProcess getResearch15_publicationprocess() {
        return research15_publicationprocess;
    }

    public void setResearch15_publicationprocess(research15_PublicationProcess research15_publicationprocess) {
        this.research15_publicationprocess = research15_publicationprocess;
    }
    public List<research15_Position> getResearch15_positions() {
        return research15_positions;
    }

    public void addResearch15_position(Research15_position research15_position) {
        this.research15_positions.add(research15_position);
    }

}