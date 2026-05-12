





import java.util.List;
import java.util.ArrayList;

public class setup_SetupTaskContainer  {






    private List<setup_SetupTask> setup_setuptasks;


    public setup_SetupTaskContainer(
    ) {
        this.setup_setuptasks = new ArrayList<>();
    }

    public setup_SetupTaskContainer(
        ArrayList<setup_SetupTask> setup_setuptasks    ) {
        this.setup_setuptasks = setup_setuptasks;
    }


    public List<setup_SetupTask> getSetup_setuptasks() {
        return setup_setuptasks;
    }

    public void addSetup_setuptask(Setup_setuptask setup_setuptask) {
        this.setup_setuptasks.add(setup_setuptask);
    }

}