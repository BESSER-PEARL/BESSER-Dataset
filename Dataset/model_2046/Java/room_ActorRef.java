





import java.util.List;
import java.util.ArrayList;

public class room_ActorRef extends ActorContainerRef {

    private int size;





    private room_ActorContainerClass room_actorcontainerclass;


    public room_ActorRef(
        int size    ) {
        super(
        );
        this.size = size;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public room_ActorContainerClass getRoom_actorcontainerclass() {
        return room_actorcontainerclass;
    }

    public void setRoom_actorcontainerclass(room_ActorContainerClass room_actorcontainerclass) {
        this.room_actorcontainerclass = room_actorcontainerclass;
    }

}