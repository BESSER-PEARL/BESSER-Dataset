





import java.util.List;
import java.util.ArrayList;

public class vql_PatternCall extends CallableRelation {






    private List<vql_ValueReference> vql_valuereferences;




    private vql_Pattern vql_pattern;


    public vql_PatternCall(
    ) {
        super(
        );
        this.vql_valuereferences = new ArrayList<>();
    }

    public vql_PatternCall(
        ArrayList<vql_ValueReference> vql_valuereferences    ) {
        this.vql_valuereferences = vql_valuereferences;
    }


    public List<vql_ValueReference> getVql_valuereferences() {
        return vql_valuereferences;
    }

    public void addVql_valuereference(Vql_valuereference vql_valuereference) {
        this.vql_valuereferences.add(vql_valuereference);
    }
    public vql_Pattern getVql_pattern() {
        return vql_pattern;
    }

    public void setVql_pattern(vql_Pattern vql_pattern) {
        this.vql_pattern = vql_pattern;
    }

}