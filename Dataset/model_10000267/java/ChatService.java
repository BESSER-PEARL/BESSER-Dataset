





import java.util.List;
import java.util.ArrayList;

public class ChatService  {

    private String attribute;
    private String attribute2;
    private None usuario;
    private String salasCollection;
    private String attribute3;
    private String itemsCollection;





    private Room_Interface room_interface;




    private Mensaje_Interface mensaje_interface;


    public ChatService(
        String attribute,        String attribute2,        None usuario,        String salasCollection,        String attribute3,        String itemsCollection    ) {
        this.attribute = attribute;
        this.attribute2 = attribute2;
        this.usuario = usuario;
        this.salasCollection = salasCollection;
        this.attribute3 = attribute3;
        this.itemsCollection = itemsCollection;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(String attribute2) {
        this.attribute2 = attribute2;
    }
    public None getUsuario() {
        return usuario;
    }

    public void setUsuario(None usuario) {
        this.usuario = usuario;
    }
    public String getSalascollection() {
        return salasCollection;
    }

    public void setSalascollection(String salasCollection) {
        this.salasCollection = salasCollection;
    }
    public String getAttribute3() {
        return attribute3;
    }

    public void setAttribute3(String attribute3) {
        this.attribute3 = attribute3;
    }
    public String getItemscollection() {
        return itemsCollection;
    }

    public void setItemscollection(String itemsCollection) {
        this.itemsCollection = itemsCollection;
    }

    public Room_Interface getRoom_interface() {
        return room_interface;
    }

    public void setRoom_interface(Room_Interface room_interface) {
        this.room_interface = room_interface;
    }
    public Mensaje_Interface getMensaje_interface() {
        return mensaje_interface;
    }

    public void setMensaje_interface(Mensaje_Interface mensaje_interface) {
        this.mensaje_interface = mensaje_interface;
    }

}