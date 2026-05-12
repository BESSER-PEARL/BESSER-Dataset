





import java.util.List;
import java.util.ArrayList;

public class Ant_PatternSet extends Set {






    private List<Ant_InExcludes> ant_inexcludess;


    public Ant_PatternSet(
    ) {
        super(
        );
        this.ant_inexcludess = new ArrayList<>();
    }

    public Ant_PatternSet(
        ArrayList<Ant_InExcludes> ant_inexcludess    ) {
        this.ant_inexcludess = ant_inexcludess;
    }


    public List<Ant_InExcludes> getAnt_inexcludess() {
        return ant_inexcludess;
    }

    public void addAnt_inexcludes(Ant_inexcludes ant_inexcludes) {
        this.ant_inexcludess.add(ant_inexcludes);
    }

}