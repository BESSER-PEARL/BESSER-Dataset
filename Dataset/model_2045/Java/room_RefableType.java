





import java.util.List;
import java.util.ArrayList;

public class room_RefableType  {

    private boolean ref;





    private room_DataType room_datatype;




    private room_VarDecl room_vardecl;


    public room_RefableType(
        boolean ref    ) {
        this.ref = ref;
    }


    public boolean getRef() {
        return ref;
    }

    public void setRef(boolean ref) {
        this.ref = ref;
    }

    public room_DataType getRoom_datatype() {
        return room_datatype;
    }

    public void setRoom_datatype(room_DataType room_datatype) {
        this.room_datatype = room_datatype;
    }
    public room_VarDecl getRoom_vardecl() {
        return room_vardecl;
    }

    public void setRoom_vardecl(room_VarDecl room_vardecl) {
        this.room_vardecl = room_vardecl;
    }

}