





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Project  {






    private List<AntTaskDef> anttaskdefs;




    private List<PrePostGoal> prepostgoals;




    private Path path;




    private List<AntProperty> antpropertys;


    public MavenMaven_Project(
    ) {
        this.anttaskdefs = new ArrayList<>();
        this.prepostgoals = new ArrayList<>();
        this.antpropertys = new ArrayList<>();
    }

    public MavenMaven_Project(
        ArrayList<AntTaskDef> anttaskdefs,        ArrayList<PrePostGoal> prepostgoals,        ArrayList<AntProperty> antpropertys    ) {
        this.anttaskdefs = anttaskdefs;
        this.prepostgoals = prepostgoals;
        this.antpropertys = antpropertys;
    }


    public List<AntTaskDef> getAnttaskdefs() {
        return anttaskdefs;
    }

    public void addAnttaskdef(Anttaskdef anttaskdef) {
        this.anttaskdefs.add(anttaskdef);
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

}