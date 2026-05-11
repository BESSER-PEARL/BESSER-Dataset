





import java.util.List;
import java.util.ArrayList;

public class room_ActorInstancePath  {

    private String segments;





    private room_LogicalThread room_logicalthread;


    public room_ActorInstancePath(
        String segments    ) {
        this.segments = segments;
    }


    public String getSegments() {
        return segments;
    }

    public void setSegments(String segments) {
        this.segments = segments;
    }

    public room_LogicalThread getRoom_logicalthread() {
        return room_logicalthread;
    }

    public void setRoom_logicalthread(room_LogicalThread room_logicalthread) {
        this.room_logicalthread = room_logicalthread;
    }

}