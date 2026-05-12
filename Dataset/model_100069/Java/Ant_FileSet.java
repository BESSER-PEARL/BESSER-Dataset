





import java.util.List;
import java.util.ArrayList;

public class Ant_FileSet extends Set {

    private String dir;





    private List<PatternSet> patternsets;




    private List<Excludes> excludess;




    private List<Includes> includess;


    public Ant_FileSet(
        String dir    ) {
        super(
        );
        this.dir = dir;
        this.patternsets = new ArrayList<>();
        this.excludess = new ArrayList<>();
        this.includess = new ArrayList<>();
    }

    public Ant_FileSet(
        String dir        ArrayList<PatternSet> patternsets,        ArrayList<Excludes> excludess,        ArrayList<Includes> includess    ) {
        this.dir = dir;
        this.patternsets = patternsets;
        this.excludess = excludess;
        this.includess = includess;
    }

    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }

    public List<PatternSet> getPatternsets() {
        return patternsets;
    }

    public void addPatternset(Patternset patternset) {
        this.patternsets.add(patternset);
    }
    public List<Excludes> getExcludess() {
        return excludess;
    }

    public void addExcludes(Excludes excludes) {
        this.excludess.add(excludes);
    }
    public List<Includes> getIncludess() {
        return includess;
    }

    public void addIncludes(Includes includes) {
        this.includess.add(includes);
    }

}