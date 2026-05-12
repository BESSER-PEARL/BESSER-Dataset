





import java.util.List;
import java.util.ArrayList;

public class research32_PublicationStructure extends Named {






    private List<research32_Researcher> research32_researchers;


    public research32_PublicationStructure(
    ) {
        super(
        );
        this.research32_researchers = new ArrayList<>();
    }

    public research32_PublicationStructure(
        ArrayList<research32_Researcher> research32_researchers    ) {
        this.research32_researchers = research32_researchers;
    }


    public List<research32_Researcher> getResearch32_researchers() {
        return research32_researchers;
    }

    public void addResearch32_researcher(Research32_researcher research32_researcher) {
        this.research32_researchers.add(research32_researcher);
    }

}