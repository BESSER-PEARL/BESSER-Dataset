





import java.util.List;
import java.util.ArrayList;

public class research13_PublicationSystem extends Named {






    private List<research13_Position> research13_positions;




    private research13_PublicationProcess research13_publicationprocess;


    public research13_PublicationSystem(
    ) {
        super(
        );
        this.research13_positions = new ArrayList<>();
    }

    public research13_PublicationSystem(
        ArrayList<research13_Position> research13_positions    ) {
        this.research13_positions = research13_positions;
    }


    public List<research13_Position> getResearch13_positions() {
        return research13_positions;
    }

    public void addResearch13_position(Research13_position research13_position) {
        this.research13_positions.add(research13_position);
    }
    public research13_PublicationProcess getResearch13_publicationprocess() {
        return research13_publicationprocess;
    }

    public void setResearch13_publicationprocess(research13_PublicationProcess research13_publicationprocess) {
        this.research13_publicationprocess = research13_publicationprocess;
    }

}