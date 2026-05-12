





import java.util.List;
import java.util.ArrayList;

public class login  {

    private String role;
    private String contrasena;
    private int loginID;
    private String usuario;





    private doctor doctor;




    private empleado empleado;


    public login(
        String role,        String contrasena,        int loginID,        String usuario    ) {
        this.role = role;
        this.contrasena = contrasena;
        this.loginID = loginID;
        this.usuario = usuario;
    }


    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }
    public String getContrasena() {
        return contrasena;
    }

    public void setContrasena(String contrasena) {
        this.contrasena = contrasena;
    }
    public int getLoginid() {
        return loginID;
    }

    public void setLoginid(int loginID) {
        this.loginID = loginID;
    }
    public String getUsuario() {
        return usuario;
    }

    public void setUsuario(String usuario) {
        this.usuario = usuario;
    }

    public doctor getDoctor() {
        return doctor;
    }

    public void setDoctor(doctor doctor) {
        this.doctor = doctor;
    }
    public empleado getEmpleado() {
        return empleado;
    }

    public void setEmpleado(empleado empleado) {
        this.empleado = empleado;
    }

}