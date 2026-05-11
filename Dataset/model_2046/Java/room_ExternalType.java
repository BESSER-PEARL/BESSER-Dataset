





import java.util.List;
import java.util.ArrayList;

public class room_ExternalType extends ComplexType {

    private String targetName;





    private room_RoomModel room_roommodel;


    public room_ExternalType(
        String targetName    ) {
        super(
        );
        this.targetName = targetName;
    }


    public String getTargetname() {
        return targetName;
    }

    public void setTargetname(String targetName) {
        this.targetName = targetName;
    }

    public room_RoomModel getRoom_roommodel() {
        return room_roommodel;
    }

    public void setRoom_roommodel(room_RoomModel room_roommodel) {
        this.room_roommodel = room_roommodel;
    }

}