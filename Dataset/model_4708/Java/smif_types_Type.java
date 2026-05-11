





import java.util.List;
import java.util.ArrayList;

public class smif_types_Type extends lexicalscope_LexicalScope, toplevel_Context {






    private RepresentationRule representationrule;




    private RepresentationRule representationrule;




    private List<MatchEnd> matchends;


    public smif_types_Type(
    ) {
        super(
        );
        this.matchends = new ArrayList<>();
    }

    public smif_types_Type(
        ArrayList<MatchEnd> matchends    ) {
        this.matchends = matchends;
    }


    public RepresentationRule getRepresentationrule() {
        return representationrule;
    }

    public void setRepresentationrule(RepresentationRule representationrule) {
        this.representationrule = representationrule;
    }
    public RepresentationRule getRepresentationrule() {
        return representationrule;
    }

    public void setRepresentationrule(RepresentationRule representationrule) {
        this.representationrule = representationrule;
    }
    public List<MatchEnd> getMatchends() {
        return matchends;
    }

    public void addMatchend(Matchend matchend) {
        this.matchends.add(matchend);
    }

}