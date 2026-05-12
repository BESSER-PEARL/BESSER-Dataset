





import java.util.List;
import java.util.ArrayList;

public class Room_Interface  {






    private List<Usuario_Interface> usuario_interfaces;


    public Room_Interface(
    ) {
        this.usuario_interfaces = new ArrayList<>();
    }

    public Room_Interface(
        ArrayList<Usuario_Interface> usuario_interfaces    ) {
        this.usuario_interfaces = usuario_interfaces;
    }


    public List<Usuario_Interface> getUsuario_interfaces() {
        return usuario_interfaces;
    }

    public void addUsuario_interface(Usuario_interface usuario_interface) {
        this.usuario_interfaces.add(usuario_interface);
    }

}