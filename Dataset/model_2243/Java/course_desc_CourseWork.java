





import java.util.List;
import java.util.ArrayList;

public class course_desc_CourseWork  {

    private boolean isMandatory;
    private boolean isRestricted;
    private int Duration;
    private String Room;
    private String Type;



    public course_desc_CourseWork(
        boolean isMandatory,        boolean isRestricted,        int Duration,        String Room,        String Type    ) {
        this.isMandatory = isMandatory;
        this.isRestricted = isRestricted;
        this.Duration = Duration;
        this.Room = Room;
        this.Type = Type;
    }


    public boolean getIsmandatory() {
        return isMandatory;
    }

    public void setIsmandatory(boolean isMandatory) {
        this.isMandatory = isMandatory;
    }
    public boolean getIsrestricted() {
        return isRestricted;
    }

    public void setIsrestricted(boolean isRestricted) {
        this.isRestricted = isRestricted;
    }
    public int getDuration() {
        return Duration;
    }

    public void setDuration(int Duration) {
        this.Duration = Duration;
    }
    public String getRoom() {
        return Room;
    }

    public void setRoom(String Room) {
        this.Room = Room;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }


}