





import java.util.List;
import java.util.ArrayList;

public class tp6_PublicationStructure  {






    private List<tp6_Researcher> tp6_researchers;


    public tp6_PublicationStructure(
    ) {
        this.tp6_researchers = new ArrayList<>();
    }

    public tp6_PublicationStructure(
        ArrayList<tp6_Researcher> tp6_researchers    ) {
        this.tp6_researchers = tp6_researchers;
    }


    public List<tp6_Researcher> getTp6_researchers() {
        return tp6_researchers;
    }

    public void addTp6_researcher(Tp6_researcher tp6_researcher) {
        this.tp6_researchers.add(tp6_researcher);
    }

}