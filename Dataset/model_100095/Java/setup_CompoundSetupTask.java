





import java.util.List;
import java.util.ArrayList;

public class setup_CompoundSetupTask extends SetupTask, SetupTaskContainer {

    private String name;



    public setup_CompoundSetupTask(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}