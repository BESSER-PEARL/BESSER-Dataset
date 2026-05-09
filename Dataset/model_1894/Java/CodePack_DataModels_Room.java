





import java.util.List;
import java.util.ArrayList;

public class CodePack_DataModels_Room  {

    private boolean isAvailable;
    private String room_type;
    private String description;
    private int number;



    public CodePack_DataModels_Room(
        boolean isAvailable,        String room_type,        String description,        int number    ) {
        this.isAvailable = isAvailable;
        this.room_type = room_type;
        this.description = description;
        this.number = number;
    }


    public boolean getIsavailable() {
        return isAvailable;
    }

    public void setIsavailable(boolean isAvailable) {
        this.isAvailable = isAvailable;
    }
    public String getRoom_type() {
        return room_type;
    }

    public void setRoom_type(String room_type) {
        this.room_type = room_type;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }


}