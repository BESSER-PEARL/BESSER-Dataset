





import java.util.List;
import java.util.ArrayList;

public class tp4_PublicationSystem extends Named {






    private tp4_PublicationProcess tp4_publicationprocess;




    private List<tp4_Keyword> tp4_keywords;




    private List<tp4_Position> tp4_positions;


    public tp4_PublicationSystem(
    ) {
        super(
        );
        this.tp4_keywords = new ArrayList<>();
        this.tp4_positions = new ArrayList<>();
    }

    public tp4_PublicationSystem(
        ArrayList<tp4_Keyword> tp4_keywords,        ArrayList<tp4_Position> tp4_positions    ) {
        this.tp4_keywords = tp4_keywords;
        this.tp4_positions = tp4_positions;
    }


    public tp4_PublicationProcess getTp4_publicationprocess() {
        return tp4_publicationprocess;
    }

    public void setTp4_publicationprocess(tp4_PublicationProcess tp4_publicationprocess) {
        this.tp4_publicationprocess = tp4_publicationprocess;
    }
    public List<tp4_Keyword> getTp4_keywords() {
        return tp4_keywords;
    }

    public void addTp4_keyword(Tp4_keyword tp4_keyword) {
        this.tp4_keywords.add(tp4_keyword);
    }
    public List<tp4_Position> getTp4_positions() {
        return tp4_positions;
    }

    public void addTp4_position(Tp4_position tp4_position) {
        this.tp4_positions.add(tp4_position);
    }

}