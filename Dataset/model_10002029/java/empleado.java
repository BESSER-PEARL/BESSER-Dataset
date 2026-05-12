





import java.util.List;
import java.util.ArrayList;

public class empleado  {

    private String apMaterno;
    private int loginID;
    private None fechaNacimiento;
    private String codigoEmpleado;
    private int nroDocumento;
    private int empleadoID;
    private String nombre;
    private String apPaterno;





    private List<consulta> consultas;


    public empleado(
        String apMaterno,        int loginID,        None fechaNacimiento,        String codigoEmpleado,        int nroDocumento,        int empleadoID,        String nombre,        String apPaterno    ) {
        this.apMaterno = apMaterno;
        this.loginID = loginID;
        this.fechaNacimiento = fechaNacimiento;
        this.codigoEmpleado = codigoEmpleado;
        this.nroDocumento = nroDocumento;
        this.empleadoID = empleadoID;
        this.nombre = nombre;
        this.apPaterno = apPaterno;
        this.consultas = new ArrayList<>();
    }

    public empleado(
        String apMaterno,        int loginID,        None fechaNacimiento,        String codigoEmpleado,        int nroDocumento,        int empleadoID,        String nombre,        String apPaterno        ArrayList<consulta> consultas    ) {
        this.apMaterno = apMaterno;
        this.loginID = loginID;
        this.fechaNacimiento = fechaNacimiento;
        this.codigoEmpleado = codigoEmpleado;
        this.nroDocumento = nroDocumento;
        this.empleadoID = empleadoID;
        this.nombre = nombre;
        this.apPaterno = apPaterno;
        this.consultas = consultas;
    }

    public String getApmaterno() {
        return apMaterno;
    }

    public void setApmaterno(String apMaterno) {
        this.apMaterno = apMaterno;
    }
    public int getLoginid() {
        return loginID;
    }

    public void setLoginid(int loginID) {
        this.loginID = loginID;
    }
    public None getFechanacimiento() {
        return fechaNacimiento;
    }

    public void setFechanacimiento(None fechaNacimiento) {
        this.fechaNacimiento = fechaNacimiento;
    }
    public String getCodigoempleado() {
        return codigoEmpleado;
    }

    public void setCodigoempleado(String codigoEmpleado) {
        this.codigoEmpleado = codigoEmpleado;
    }
    public int getNrodocumento() {
        return nroDocumento;
    }

    public void setNrodocumento(int nroDocumento) {
        this.nroDocumento = nroDocumento;
    }
    public int getEmpleadoid() {
        return empleadoID;
    }

    public void setEmpleadoid(int empleadoID) {
        this.empleadoID = empleadoID;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getAppaterno() {
        return apPaterno;
    }

    public void setAppaterno(String apPaterno) {
        this.apPaterno = apPaterno;
    }

    public List<consulta> getConsultas() {
        return consultas;
    }

    public void addConsulta(Consulta consulta) {
        this.consultas.add(consulta);
    }

}