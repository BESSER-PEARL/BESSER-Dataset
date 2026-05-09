





import java.util.List;
import java.util.ArrayList;

public class tp4_PublicationSystem extends Named {






    private List<tp4_Position> tp4_positions;




    private tp4_PublicationStructure tp4_publicationstructure;




    private List<tp4_Keyword> tp4_keywords;




    private tp4_PublicationProcess tp4_publicationprocess;


    public tp4_PublicationSystem(
    ) {
        super(
        );
        this.tp4_positions = new ArrayList<>();
        this.tp4_keywords = new ArrayList<>();
    }

    public tp4_PublicationSystem(
        ArrayList<tp4_Position> tp4_positions,        ArrayList<tp4_Keyword> tp4_keywords    ) {
        this.tp4_positions = tp4_positions;
        this.tp4_keywords = tp4_keywords;
    }


    public List<tp4_Position> getTp4_positions() {
        return tp4_positions;
    }

    public void addTp4_position(Tp4_position tp4_position) {
        this.tp4_positions.add(tp4_position);
    }
    public tp4_PublicationStructure getTp4_publicationstructure() {
        return tp4_publicationstructure;
    }

    public void setTp4_publicationstructure(tp4_PublicationStructure tp4_publicationstructure) {
        this.tp4_publicationstructure = tp4_publicationstructure;
    }
    public List<tp4_Keyword> getTp4_keywords() {
        return tp4_keywords;
    }

    public void addTp4_keyword(Tp4_keyword tp4_keyword) {
        this.tp4_keywords.add(tp4_keyword);
    }
    public tp4_PublicationProcess getTp4_publicationprocess() {
        return tp4_publicationprocess;
    }

    public void setTp4_publicationprocess(tp4_PublicationProcess tp4_publicationprocess) {
        this.tp4_publicationprocess = tp4_publicationprocess;
    }

}