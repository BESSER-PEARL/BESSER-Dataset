





import java.util.List;
import java.util.ArrayList;

public class tp5_PublicationStructure  {






    private List<tp5_Paper> tp5_papers;




    private List<tp5_Researcher> tp5_researchers;




    private List<tp5_Position> tp5_positions;


    public tp5_PublicationStructure(
    ) {
        this.tp5_papers = new ArrayList<>();
        this.tp5_researchers = new ArrayList<>();
        this.tp5_positions = new ArrayList<>();
    }

    public tp5_PublicationStructure(
        ArrayList<tp5_Paper> tp5_papers,        ArrayList<tp5_Researcher> tp5_researchers,        ArrayList<tp5_Position> tp5_positions    ) {
        this.tp5_papers = tp5_papers;
        this.tp5_researchers = tp5_researchers;
        this.tp5_positions = tp5_positions;
    }


    public List<tp5_Paper> getTp5_papers() {
        return tp5_papers;
    }

    public void addTp5_paper(Tp5_paper tp5_paper) {
        this.tp5_papers.add(tp5_paper);
    }
    public List<tp5_Researcher> getTp5_researchers() {
        return tp5_researchers;
    }

    public void addTp5_researcher(Tp5_researcher tp5_researcher) {
        this.tp5_researchers.add(tp5_researcher);
    }
    public List<tp5_Position> getTp5_positions() {
        return tp5_positions;
    }

    public void addTp5_position(Tp5_position tp5_position) {
        this.tp5_positions.add(tp5_position);
    }

}