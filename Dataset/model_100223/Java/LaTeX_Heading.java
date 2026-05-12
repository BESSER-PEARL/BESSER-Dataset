





import java.util.List;
import java.util.ArrayList;

public class LaTeX_Heading  {






    private List<Organisation> organisations;


    public LaTeX_Heading(
    ) {
        this.organisations = new ArrayList<>();
    }

    public LaTeX_Heading(
        ArrayList<Organisation> organisations    ) {
        this.organisations = organisations;
    }


    public List<Organisation> getOrganisations() {
        return organisations;
    }

    public void addOrganisation(Organisation organisation) {
        this.organisations.add(organisation);
    }

}