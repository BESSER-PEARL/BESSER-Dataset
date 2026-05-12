





import java.util.List;
import java.util.ArrayList;

public class publication2014b_PublicationStructure extends Named {






    private List<publication2014b_Researcher> publication2014b_researchers;


    public publication2014b_PublicationStructure(
    ) {
        super(
        );
        this.publication2014b_researchers = new ArrayList<>();
    }

    public publication2014b_PublicationStructure(
        ArrayList<publication2014b_Researcher> publication2014b_researchers    ) {
        this.publication2014b_researchers = publication2014b_researchers;
    }


    public List<publication2014b_Researcher> getPublication2014b_researchers() {
        return publication2014b_researchers;
    }

    public void addPublication2014b_researcher(Publication2014b_researcher publication2014b_researcher) {
        this.publication2014b_researchers.add(publication2014b_researcher);
    }

}