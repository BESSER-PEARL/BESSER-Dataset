





import java.util.List;
import java.util.ArrayList;

public class Cliente  {

    private String foto;
    private int celular;
    private int telefono;
    private String pass;
    private String correo;
    private boolean estado;
    private String user;
    private int id;





    private List<Cuenta_external> cuenta_externals;


    public Cliente(
        String foto,        int celular,        int telefono,        String pass,        String correo,        boolean estado,        String user,        int id    ) {
        this.foto = foto;
        this.celular = celular;
        this.telefono = telefono;
        this.pass = pass;
        this.correo = correo;
        this.estado = estado;
        this.user = user;
        this.id = id;
        this.cuenta_externals = new ArrayList<>();
    }

    public Cliente(
        String foto,        int celular,        int telefono,        String pass,        String correo,        boolean estado,        String user,        int id        ArrayList<Cuenta_external> cuenta_externals    ) {
        this.foto = foto;
        this.celular = celular;
        this.telefono = telefono;
        this.pass = pass;
        this.correo = correo;
        this.estado = estado;
        this.user = user;
        this.id = id;
        this.cuenta_externals = cuenta_externals;
    }

    public String getFoto() {
        return foto;
    }

    public void setFoto(String foto) {
        this.foto = foto;
    }
    public int getCelular() {
        return celular;
    }

    public void setCelular(int celular) {
        this.celular = celular;
    }
    public int getTelefono() {
        return telefono;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }
    public String getPass() {
        return pass;
    }

    public void setPass(String pass) {
        this.pass = pass;
    }
    public String getCorreo() {
        return correo;
    }

    public void setCorreo(String correo) {
        this.correo = correo;
    }
    public boolean getEstado() {
        return estado;
    }

    public void setEstado(boolean estado) {
        this.estado = estado;
    }
    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public List<Cuenta_external> getCuenta_externals() {
        return cuenta_externals;
    }

    public void addCuenta_external(Cuenta_external cuenta_external) {
        this.cuenta_externals.add(cuenta_external);
    }

}