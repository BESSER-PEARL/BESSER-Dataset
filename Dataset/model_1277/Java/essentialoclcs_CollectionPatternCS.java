





import java.util.List;
import java.util.ArrayList;

public class essentialoclcs_CollectionPatternCS extends TypedRefCS {

    private String restVariableName;





    private essentialoclcs_ExpCS essentialoclcs_expcs;




    private List<essentialoclcs_PatternExpCS> essentialoclcs_patternexpcss;


    public essentialoclcs_CollectionPatternCS(
        String restVariableName    ) {
        super(
        );
        this.restVariableName = restVariableName;
        this.essentialoclcs_patternexpcss = new ArrayList<>();
    }

    public essentialoclcs_CollectionPatternCS(
        String restVariableName        ArrayList<essentialoclcs_PatternExpCS> essentialoclcs_patternexpcss    ) {
        this.restVariableName = restVariableName;
        this.essentialoclcs_patternexpcss = essentialoclcs_patternexpcss;
    }

    public String getRestvariablename() {
        return restVariableName;
    }

    public void setRestvariablename(String restVariableName) {
        this.restVariableName = restVariableName;
    }

    public essentialoclcs_ExpCS getEssentialoclcs_expcs() {
        return essentialoclcs_expcs;
    }

    public void setEssentialoclcs_expcs(essentialoclcs_ExpCS essentialoclcs_expcs) {
        this.essentialoclcs_expcs = essentialoclcs_expcs;
    }
    public List<essentialoclcs_PatternExpCS> getEssentialoclcs_patternexpcss() {
        return essentialoclcs_patternexpcss;
    }

    public void addEssentialoclcs_patternexpcs(Essentialoclcs_patternexpcs essentialoclcs_patternexpcs) {
        this.essentialoclcs_patternexpcss.add(essentialoclcs_patternexpcs);
    }

}