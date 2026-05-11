





import java.util.List;
import java.util.ArrayList;

public class NBVR_Logic_Predicate  {

    private String name;





    private VocVerb vocverb;




    private List<RoleVariable> rolevariables;




    private VocNoun vocnoun;


    public NBVR_Logic_Predicate(
        String name    ) {
        this.name = name;
        this.rolevariables = new ArrayList<>();
    }

    public NBVR_Logic_Predicate(
        String name        ArrayList<RoleVariable> rolevariables    ) {
        this.name = name;
        this.rolevariables = rolevariables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public VocVerb getVocverb() {
        return vocverb;
    }

    public void setVocverb(VocVerb vocverb) {
        this.vocverb = vocverb;
    }
    public List<RoleVariable> getRolevariables() {
        return rolevariables;
    }

    public void addRolevariable(Rolevariable rolevariable) {
        this.rolevariables.add(rolevariable);
    }
    public VocNoun getVocnoun() {
        return vocnoun;
    }

    public void setVocnoun(VocNoun vocnoun) {
        this.vocnoun = vocnoun;
    }

}