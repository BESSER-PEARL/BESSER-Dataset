





import java.util.List;
import java.util.ArrayList;

public class room_Message  {

    private boolean priv;
    private String name;





    private room_Documentation room_documentation;




    private room_PortOperation room_portoperation;




    private room_VarDecl room_vardecl;


    public room_Message(
        boolean priv,        String name    ) {
        this.priv = priv;
        this.name = name;
    }


    public boolean getPriv() {
        return priv;
    }

    public void setPriv(boolean priv) {
        this.priv = priv;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public room_Documentation getRoom_documentation() {
        return room_documentation;
    }

    public void setRoom_documentation(room_Documentation room_documentation) {
        this.room_documentation = room_documentation;
    }
    public room_PortOperation getRoom_portoperation() {
        return room_portoperation;
    }

    public void setRoom_portoperation(room_PortOperation room_portoperation) {
        this.room_portoperation = room_portoperation;
    }
    public room_VarDecl getRoom_vardecl() {
        return room_vardecl;
    }

    public void setRoom_vardecl(room_VarDecl room_vardecl) {
        this.room_vardecl = room_vardecl;
    }

}