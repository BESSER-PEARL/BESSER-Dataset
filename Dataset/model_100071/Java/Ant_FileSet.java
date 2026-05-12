





import java.util.List;
import java.util.ArrayList;

public class Ant_FileSet extends Set {

    private String dir;





    private Ant_ClassPath ant_classpath;




    private List<Ant_Excludes> ant_excludess;




    private List<Ant_PatternSet> ant_patternsets;




    private List<Ant_Includes> ant_includess;




    private Ant_Path ant_path;


    public Ant_FileSet(
        String dir    ) {
        super(
        );
        this.dir = dir;
        this.ant_excludess = new ArrayList<>();
        this.ant_patternsets = new ArrayList<>();
        this.ant_includess = new ArrayList<>();
    }

    public Ant_FileSet(
        String dir        ArrayList<Ant_Excludes> ant_excludess,        ArrayList<Ant_PatternSet> ant_patternsets,        ArrayList<Ant_Includes> ant_includess    ) {
        this.dir = dir;
        this.ant_excludess = ant_excludess;
        this.ant_patternsets = ant_patternsets;
        this.ant_includess = ant_includess;
    }

    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }

    public Ant_ClassPath getAnt_classpath() {
        return ant_classpath;
    }

    public void setAnt_classpath(Ant_ClassPath ant_classpath) {
        this.ant_classpath = ant_classpath;
    }
    public List<Ant_Excludes> getAnt_excludess() {
        return ant_excludess;
    }

    public void addAnt_excludes(Ant_excludes ant_excludes) {
        this.ant_excludess.add(ant_excludes);
    }
    public List<Ant_PatternSet> getAnt_patternsets() {
        return ant_patternsets;
    }

    public void addAnt_patternset(Ant_patternset ant_patternset) {
        this.ant_patternsets.add(ant_patternset);
    }
    public List<Ant_Includes> getAnt_includess() {
        return ant_includess;
    }

    public void addAnt_includes(Ant_includes ant_includes) {
        this.ant_includess.add(ant_includes);
    }
    public Ant_Path getAnt_path() {
        return ant_path;
    }

    public void setAnt_path(Ant_Path ant_path) {
        this.ant_path = ant_path;
    }

}