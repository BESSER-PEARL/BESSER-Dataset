





import java.util.List;
import java.util.ArrayList;

public class tp4_PublicationStructure extends Named {






    private List<tp4_Paper> tp4_papers;


    public tp4_PublicationStructure(
    ) {
        super(
        );
        this.tp4_papers = new ArrayList<>();
    }

    public tp4_PublicationStructure(
        ArrayList<tp4_Paper> tp4_papers    ) {
        this.tp4_papers = tp4_papers;
    }


    public List<tp4_Paper> getTp4_papers() {
        return tp4_papers;
    }

    public void addTp4_paper(Tp4_paper tp4_paper) {
        this.tp4_papers.add(tp4_paper);
    }

}