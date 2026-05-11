





import java.util.List;
import java.util.ArrayList;

public class room_Type  {

    private String prim;





    private room_Attribute room_attribute;




    private room_DataClass room_dataclass;




    private room_TypedID room_typedid;


    public room_Type(
        String prim    ) {
        this.prim = prim;
    }


    public String getPrim() {
        return prim;
    }

    public void setPrim(String prim) {
        this.prim = prim;
    }

    public room_Attribute getRoom_attribute() {
        return room_attribute;
    }

    public void setRoom_attribute(room_Attribute room_attribute) {
        this.room_attribute = room_attribute;
    }
    public room_DataClass getRoom_dataclass() {
        return room_dataclass;
    }

    public void setRoom_dataclass(room_DataClass room_dataclass) {
        this.room_dataclass = room_dataclass;
    }
    public room_TypedID getRoom_typedid() {
        return room_typedid;
    }

    public void setRoom_typedid(room_TypedID room_typedid) {
        this.room_typedid = room_typedid;
    }

}