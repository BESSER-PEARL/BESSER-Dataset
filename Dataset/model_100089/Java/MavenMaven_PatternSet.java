





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_PatternSet extends Set {






    private List<InExcludes> inexcludess;


    public MavenMaven_PatternSet(
    ) {
        super(
        );
        this.inexcludess = new ArrayList<>();
    }

    public MavenMaven_PatternSet(
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