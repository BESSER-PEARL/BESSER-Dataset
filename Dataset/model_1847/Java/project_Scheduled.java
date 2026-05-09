





import java.util.List;
import java.util.ArrayList;

public class project_Scheduled extends TaskAttribute {

    private boolean scheduled;



    public project_Scheduled(
        boolean scheduled    ) {
        super(
        );
        this.scheduled = scheduled;
    }


    public boolean getScheduled() {
        return scheduled;
    }

    public void setScheduled(boolean scheduled) {
        this.scheduled = scheduled;
    }


}