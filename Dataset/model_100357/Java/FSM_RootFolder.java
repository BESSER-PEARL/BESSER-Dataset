





import java.util.List;
import java.util.ArrayList;

public class FSM_RootFolder  {

    private String name;





    private List<RootFolder> rootfolders;




    private List<StateMachine> statemachines;


    public FSM_RootFolder(
        String name    ) {
        this.name = name;
        this.rootfolders = new ArrayList<>();
        this.statemachines = new ArrayList<>();
    }

    public FSM_RootFolder(
        String name        ArrayList<RootFolder> rootfolders,        ArrayList<StateMachine> statemachines    ) {
        this.name = name;
        this.rootfolders = rootfolders;
        this.statemachines = statemachines;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<RootFolder> getRootfolders() {
        return rootfolders;
    }

    public void addRootfolder(Rootfolder rootfolder) {
        this.rootfolders.add(rootfolder);
    }
    public List<StateMachine> getStatemachines() {
        return statemachines;
    }

    public void addStatemachine(Statemachine statemachine) {
        this.statemachines.add(statemachine);
    }

}