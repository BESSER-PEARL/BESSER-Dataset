





import java.util.List;
import java.util.ArrayList;

public class model_meeting_MeetingSection extends UnicaseModelElement {

    private int allocatedTime;



    public model_meeting_MeetingSection(
        int allocatedTime    ) {
        super(
        );
        this.allocatedTime = allocatedTime;
    }


    public int getAllocatedtime() {
        return allocatedTime;
    }

    public void setAllocatedtime(int allocatedTime) {
        this.allocatedTime = allocatedTime;
    }


}