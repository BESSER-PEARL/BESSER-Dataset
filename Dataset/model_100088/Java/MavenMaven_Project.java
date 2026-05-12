





import java.util.List;
import java.util.ArrayList;

public class MavenMaven_Project  {






    private List<MavenMaven_AntTaskDef> mavenmaven_anttaskdefs;




    private List<MavenMaven_AntProperty> mavenmaven_antpropertys;




    private List<MavenMaven_PrePostGoal> mavenmaven_prepostgoals;


    public MavenMaven_Project(
    ) {
        this.mavenmaven_anttaskdefs = new ArrayList<>();
        this.mavenmaven_antpropertys = new ArrayList<>();
        this.mavenmaven_prepostgoals = new ArrayList<>();
    }

    public MavenMaven_Project(
        ArrayList<MavenMaven_AntTaskDef> mavenmaven_anttaskdefs,        ArrayList<MavenMaven_AntProperty> mavenmaven_antpropertys,        ArrayList<MavenMaven_PrePostGoal> mavenmaven_prepostgoals    ) {
        this.mavenmaven_anttaskdefs = mavenmaven_anttaskdefs;
        this.mavenmaven_antpropertys = mavenmaven_antpropertys;
        this.mavenmaven_prepostgoals = mavenmaven_prepostgoals;
    }


    public List<MavenMaven_AntTaskDef> getMavenmaven_anttaskdefs() {
        return mavenmaven_anttaskdefs;
    }

    public void addMavenmaven_anttaskdef(Mavenmaven_anttaskdef mavenmaven_anttaskdef) {
        this.mavenmaven_anttaskdefs.add(mavenmaven_anttaskdef);
    }
    public List<MavenMaven_AntProperty> getMavenmaven_antpropertys() {
        return mavenmaven_antpropertys;
    }

    public void addMavenmaven_antproperty(Mavenmaven_antproperty mavenmaven_antproperty) {
        this.mavenmaven_antpropertys.add(mavenmaven_antproperty);
    }
    public List<MavenMaven_PrePostGoal> getMavenmaven_prepostgoals() {
        return mavenmaven_prepostgoals;
    }

    public void addMavenmaven_prepostgoal(Mavenmaven_prepostgoal mavenmaven_prepostgoal) {
        this.mavenmaven_prepostgoals.add(mavenmaven_prepostgoal);
    }

}