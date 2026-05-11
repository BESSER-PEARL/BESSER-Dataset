





import java.util.List;
import java.util.ArrayList;

public class room_Message  {

    private String name;
    private boolean priv;





    private room_ProtocolClass room_protocolclass;




    private room_PortOperation room_portoperation;




    private room_ProtocolClass room_protocolclass;




    private room_VarDecl room_vardecl;


    public room_Message(
        String name,        boolean priv    ) {
        this.name = name;
        this.priv = priv;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getPriv() {
        return priv;
    }

    public void setPriv(boolean priv) {
        this.priv = priv;
    }

    public room_ProtocolClass getRoom_protocolclass() {
        return room_protocolclass;
    }

    public void setRoom_protocolclass(room_ProtocolClass room_protocolclass) {
        this.room_protocolclass = room_protocolclass;
    }
    public room_PortOperation getRoom_portoperation() {
        return room_portoperation;
    }

    public void setRoom_portoperation(room_PortOperation room_portoperation) {
        this.room_portoperation = room_portoperation;
    }
    public room_ProtocolClass getRoom_protocolclass() {
        return room_protocolclass;
    }

    public void setRoom_protocolclass(room_ProtocolClass room_protocolclass) {
        this.room_protocolclass = room_protocolclass;
    }
    public room_VarDecl getRoom_vardecl() {
        return room_vardecl;
    }

    public void setRoom_vardecl(room_VarDecl room_vardecl) {
        this.room_vardecl = room_vardecl;
    }

}