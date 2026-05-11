





import java.util.List;
import java.util.ArrayList;

public class tracker_ReplacedTag extends Event {

    private boolean usainNumberUsedForOldId;
    private String oldId;





    private tracker_Tag tracker_tag;


    public tracker_ReplacedTag(
        boolean usainNumberUsedForOldId,        String oldId    ) {
        super(
        );
        this.usainNumberUsedForOldId = usainNumberUsedForOldId;
        this.oldId = oldId;
    }


    public boolean getUsainnumberusedforoldid() {
        return usainNumberUsedForOldId;
    }

    public void setUsainnumberusedforoldid(boolean usainNumberUsedForOldId) {
        this.usainNumberUsedForOldId = usainNumberUsedForOldId;
    }
    public String getOldid() {
        return oldId;
    }

    public void setOldid(String oldId) {
        this.oldId = oldId;
    }

    public tracker_Tag getTracker_tag() {
        return tracker_tag;
    }

    public void setTracker_tag(tracker_Tag tracker_tag) {
        this.tracker_tag = tracker_tag;
    }

}