





import java.util.List;
import java.util.ArrayList;

public class room_Documentation  {

    private String text;





    private room_RoomModel room_roommodel;


    public room_Documentation(
        String text    ) {
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public room_RoomModel getRoom_roommodel() {
        return room_roommodel;
    }

    public void setRoom_roommodel(room_RoomModel room_roommodel) {
        this.room_roommodel = room_roommodel;
    }

}