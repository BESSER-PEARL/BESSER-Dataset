





import java.util.List;
import java.util.ArrayList;

public class frontend_mappings_Context extends LocatedElement {






    private List<Tag> tags;




    private List<MatchedElement> matchedelements;




    private List<MatchedElement> matchedelements;


    public frontend_mappings_Context(
    ) {
        super(
        );
        this.tags = new ArrayList<>();
        this.matchedelements = new ArrayList<>();
        this.matchedelements = new ArrayList<>();
    }

    public frontend_mappings_Context(
        ArrayList<Tag> tags,        ArrayList<MatchedElement> matchedelements,        ArrayList<MatchedElement> matchedelements    ) {
        this.tags = tags;
        this.matchedelements = matchedelements;
        this.matchedelements = matchedelements;
    }


    public List<Tag> getTags() {
        return tags;
    }

    public void addTag(Tag tag) {
        this.tags.add(tag);
    }
    public List<MatchedElement> getMatchedelements() {
        return matchedelements;
    }

    public void addMatchedelement(Matchedelement matchedelement) {
        this.matchedelements.add(matchedelement);
    }
    public List<MatchedElement> getMatchedelements() {
        return matchedelements;
    }

    public void addMatchedelement(Matchedelement matchedelement) {
        this.matchedelements.add(matchedelement);
    }

}