





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private String Room_number;
    private String Room_description;
    private String Room_Id;
    private String Room_type;





    private Admin admin;


    public Room(
        String Room_number,        String Room_description,        String Room_Id,        String Room_type    ) {
        this.Room_number = Room_number;
        this.Room_description = Room_description;
        this.Room_Id = Room_Id;
        this.Room_type = Room_type;
    }


    public String getRoom_number() {
        return Room_number;
    }

    public void setRoom_number(String Room_number) {
        this.Room_number = Room_number;
    }
    public String getRoom_description() {
        return Room_description;
    }

    public void setRoom_description(String Room_description) {
        this.Room_description = Room_description;
    }
    public String getRoom_id() {
        return Room_Id;
    }

    public void setRoom_id(String Room_Id) {
        this.Room_Id = Room_Id;
    }
    public String getRoom_type() {
        return Room_type;
    }

    public void setRoom_type(String Room_type) {
        this.Room_type = Room_type;
    }

    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }

}