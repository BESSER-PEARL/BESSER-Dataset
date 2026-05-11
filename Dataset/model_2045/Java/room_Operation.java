





import java.util.List;
import java.util.ArrayList;

public class room_Operation  {

    private String name;





    private room_DetailCode room_detailcode;




    private room_RefableType room_refabletype;




    private List<room_VarDecl> room_vardecls;


    public room_Operation(
        String name    ) {
        this.name = name;
        this.room_vardecls = new ArrayList<>();
    }

    public room_Operation(
        String name        ArrayList<room_VarDecl> room_vardecls    ) {
        this.name = name;
        this.room_vardecls = room_vardecls;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public room_DetailCode getRoom_detailcode() {
        return room_detailcode;
    }

    public void setRoom_detailcode(room_DetailCode room_detailcode) {
        this.room_detailcode = room_detailcode;
    }
    public room_RefableType getRoom_refabletype() {
        return room_refabletype;
    }

    public void setRoom_refabletype(room_RefableType room_refabletype) {
        this.room_refabletype = room_refabletype;
    }
    public List<room_VarDecl> getRoom_vardecls() {
        return room_vardecls;
    }

    public void addRoom_vardecl(Room_vardecl room_vardecl) {
        this.room_vardecls.add(room_vardecl);
    }

}