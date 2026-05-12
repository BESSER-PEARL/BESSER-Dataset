





import java.util.List;
import java.util.ArrayList;

public class Ant_PatternSet extends Set {






    private List<InExcludes> inexcludess;


    public Ant_PatternSet(
    ) {
        super(
        );
        this.inexcludess = new ArrayList<>();
    }

    public Ant_PatternSet(
        ArrayList<InExcludes> inexcludess    ) {
        this.inexcludess = inexcludess;
    }


    public List<InExcludes> getInexcludess() {
        return inexcludess;
    }

    public void addInexcludes(Inexcludes inexcludes) {
        this.inexcludess.add(inexcludes);
    }

}