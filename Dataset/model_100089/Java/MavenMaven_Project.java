





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Project  {






    private List<PrePostGoal> prepostgoals;




    private Path path;




    private List<AntProperty> antpropertys;




    private List<AntTaskDef> anttaskdefs;


    public MavenMaven_Project(
    ) {
        this.prepostgoals = new ArrayList<>();
        this.antpropertys = new ArrayList<>();
        this.anttaskdefs = new ArrayList<>();
    }

    public MavenMaven_Project(
        ArrayList<PrePostGoal> prepostgoals,        ArrayList<AntProperty> antpropertys,        ArrayList<AntTaskDef> anttaskdefs    ) {
        this.prepostgoals = prepostgoals;
        this.antpropertys = antpropertys;
        this.anttaskdefs = anttaskdefs;
    }


    public List<PrePostGoal> getPrepostgoals() {
        return prepostgoals;
    }

    public void addPrepostgoal(Prepostgoal prepostgoal) {
        this.prepostgoals.add(prepostgoal);
    }
    public Path getPath() {
        return path;
    }

    public void setPath(Path path) {
        this.path = path;
    }
    public List<AntProperty> getAntpropertys() {
        return antpropertys;
    }

    public void addAntproperty(Antproperty antproperty) {
        this.antpropertys.add(antproperty);
    }
    public List<AntTaskDef> getAnttaskdefs() {
        return anttaskdefs;
    }

    public void addAnttaskdef(Anttaskdef anttaskdef) {
        this.anttaskdefs.add(anttaskdef);
    }

}