





import java.util.List;
import java.util.ArrayList;

public class setup_TargetPlatformTask extends SetupTask {

    private String name;



    public setup_TargetPlatformTask(
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