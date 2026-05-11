





import java.util.List;
import java.util.ArrayList;

public class behavioral_elements_collaborations_AssociationRole extends Association {






    private List<Link> links;


    public behavioral_elements_collaborations_AssociationRole(
    ) {
        super(
        );
        this.links = new ArrayList<>();
    }

    public behavioral_elements_collaborations_AssociationRole(
        ArrayList<Link> links    ) {
        this.links = links;
    }


    public List<Link> getLinks() {
        return links;
    }

    public void addLink(Link link) {
        this.links.add(link);
    }

}