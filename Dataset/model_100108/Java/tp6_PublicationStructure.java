





import java.util.List;
import java.util.ArrayList;

public class tp6_PublicationStructure  {






    private List<tp6_Researcher> tp6_researchers;




    private tp6_KnowledgeManager tp6_knowledgemanager;




    private List<tp6_Paper> tp6_papers;




    private List<tp6_Position> tp6_positions;


    public tp6_PublicationStructure(
    ) {
        this.tp6_researchers = new ArrayList<>();
        this.tp6_papers = new ArrayList<>();
        this.tp6_positions = new ArrayList<>();
    }

    public tp6_PublicationStructure(
        ArrayList<tp6_Researcher> tp6_researchers,        ArrayList<tp6_Paper> tp6_papers,        ArrayList<tp6_Position> tp6_positions    ) {
        this.tp6_researchers = tp6_researchers;
        this.tp6_papers = tp6_papers;
        this.tp6_positions = tp6_positions;
    }


    public List<tp6_Researcher> getTp6_researchers() {
        return tp6_researchers;
    }

    public void addTp6_researcher(Tp6_researcher tp6_researcher) {
        this.tp6_researchers.add(tp6_researcher);
    }
    public tp6_KnowledgeManager getTp6_knowledgemanager() {
        return tp6_knowledgemanager;
    }

    public void setTp6_knowledgemanager(tp6_KnowledgeManager tp6_knowledgemanager) {
        this.tp6_knowledgemanager = tp6_knowledgemanager;
    }
    public List<tp6_Paper> getTp6_papers() {
        return tp6_papers;
    }

    public void addTp6_paper(Tp6_paper tp6_paper) {
        this.tp6_papers.add(tp6_paper);
    }
    public List<tp6_Position> getTp6_positions() {
        return tp6_positions;
    }

    public void addTp6_position(Tp6_position tp6_position) {
        this.tp6_positions.add(tp6_position);
    }

}