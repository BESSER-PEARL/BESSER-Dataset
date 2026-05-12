





import java.util.List;
import java.util.ArrayList;

public class research31_PublicationStructure extends Named {






    private List<research31_Researcher> research31_researchers;


    public research31_PublicationStructure(
    ) {
        super(
        );
        this.research31_researchers = new ArrayList<>();
    }

    public research31_PublicationStructure(
        ArrayList<research31_Researcher> research31_researchers    ) {
        this.research31_researchers = research31_researchers;
    }


    public List<research31_Researcher> getResearch31_researchers() {
        return research31_researchers;
    }

    public void addResearch31_researcher(Research31_researcher research31_researcher) {
        this.research31_researchers.add(research31_researcher);
    }

}