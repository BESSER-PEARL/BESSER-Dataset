





import java.util.List;
import java.util.ArrayList;

public class Login  {






    private List<Usuario> usuarios;




    private Database database;


    public Login(
    ) {
        this.usuarios = new ArrayList<>();
    }

    public Login(
        ArrayList<Usuario> usuarios    ) {
        this.usuarios = usuarios;
    }


    public List<Usuario> getUsuarios() {
        return usuarios;
    }

    public void addUsuario(Usuario usuario) {
        this.usuarios.add(usuario);
    }
    public Database getDatabase() {
        return database;
    }

    public void setDatabase(Database database) {
        this.database = database;
    }

}