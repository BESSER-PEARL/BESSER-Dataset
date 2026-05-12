





import java.util.List;
import java.util.ArrayList;

public class research19_PublicationSystem extends Named {






    private List<research19_Position> research19_positions;




    private research19_PublicationProcess research19_publicationprocess;


    public research19_PublicationSystem(
    ) {
        super(
        );
        this.research19_positions = new ArrayList<>();
    }

    public research19_PublicationSystem(
        ArrayList<research19_Position> research19_positions    ) {
        this.research19_positions = research19_positions;
    }


    public List<research19_Position> getResearch19_positions() {
        return research19_positions;
    }

    public void addResearch19_position(Research19_position research19_position) {
        this.research19_positions.add(research19_position);
    }
    public research19_PublicationProcess getResearch19_publicationprocess() {
        return research19_publicationprocess;
    }

    public void setResearch19_publicationprocess(research19_PublicationProcess research19_publicationprocess) {
        this.research19_publicationprocess = research19_publicationprocess;
    }

}