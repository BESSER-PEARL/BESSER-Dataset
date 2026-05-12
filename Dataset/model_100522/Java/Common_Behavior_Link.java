





import java.util.List;
import java.util.ArrayList;

public class Common_Behavior_Link extends ModelElement {






    private List<LinkEnd> linkends;


    public Common_Behavior_Link(
    ) {
        super(
        );
        this.linkends = new ArrayList<>();
    }

    public Common_Behavior_Link(
        ArrayList<LinkEnd> linkends    ) {
        this.linkends = linkends;
    }


    public List<LinkEnd> getLinkends() {
        return linkends;
    }

    public void addLinkend(Linkend linkend) {
        this.linkends.add(linkend);
    }

}