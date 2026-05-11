





import java.util.List;
import java.util.ArrayList;

public class room_FreeType  {

    private String type;
    private String prim;





    private room_FreeTypedID room_freetypedid;


    public room_FreeType(
        String type,        String prim    ) {
        this.type = type;
        this.prim = prim;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getPrim() {
        return prim;
    }

    public void setPrim(String prim) {
        this.prim = prim;
    }

    public room_FreeTypedID getRoom_freetypedid() {
        return room_freetypedid;
    }

    public void setRoom_freetypedid(room_FreeTypedID room_freetypedid) {
        this.room_freetypedid = room_freetypedid;
    }

}