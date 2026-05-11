





import java.util.List;
import java.util.ArrayList;

public class smif_patterns_PatternVariable extends constraints_Conditional, properties_OwnedPropertyType {

    private String explicit;
    private String qualification;





    private List<MatchEnd> matchends;


    public smif_patterns_PatternVariable(
        String explicit,        String qualification    ) {
        super(
        );
        this.explicit = explicit;
        this.qualification = qualification;
        this.matchends = new ArrayList<>();
    }

    public smif_patterns_PatternVariable(
        String explicit,        String qualification        ArrayList<MatchEnd> matchends    ) {
        this.explicit = explicit;
        this.qualification = qualification;
        this.matchends = matchends;
    }

    public String getExplicit() {
        return explicit;
    }

    public void setExplicit(String explicit) {
        this.explicit = explicit;
    }
    public String getQualification() {
        return qualification;
    }

    public void setQualification(String qualification) {
        this.qualification = qualification;
    }

    public List<MatchEnd> getMatchends() {
        return matchends;
    }

    public void addMatchend(Matchend matchend) {
        this.matchends.add(matchend);
    }

}