





import java.util.List;
import java.util.ArrayList;

public class doctor  {

    private None fechaNacimiento;
    private int doctorID;
    private String apPaterno;
    private String nombre;
    private String codigoDoctor;
    private int especialidadID;
    private String apMaterno;
    private int nroDocumento;
    private int loginID;





    private List<consulta> consultas;


    public doctor(
        None fechaNacimiento,        int doctorID,        String apPaterno,        String nombre,        String codigoDoctor,        int especialidadID,        String apMaterno,        int nroDocumento,        int loginID    ) {
        this.fechaNacimiento = fechaNacimiento;
        this.doctorID = doctorID;
        this.apPaterno = apPaterno;
        this.nombre = nombre;
        this.codigoDoctor = codigoDoctor;
        this.especialidadID = especialidadID;
        this.apMaterno = apMaterno;
        this.nroDocumento = nroDocumento;
        this.loginID = loginID;
        this.consultas = new ArrayList<>();
    }

    public doctor(
        None fechaNacimiento,        int doctorID,        String apPaterno,        String nombre,        String codigoDoctor,        int especialidadID,        String apMaterno,        int nroDocumento,        int loginID        ArrayList<consulta> consultas    ) {
        this.fechaNacimiento = fechaNacimiento;
        this.doctorID = doctorID;
        this.apPaterno = apPaterno;
        this.nombre = nombre;
        this.codigoDoctor = codigoDoctor;
        this.especialidadID = especialidadID;
        this.apMaterno = apMaterno;
        this.nroDocumento = nroDocumento;
        this.loginID = loginID;
        this.consultas = consultas;
    }

    public None getFechanacimiento() {
        return fechaNacimiento;
    }

    public void setFechanacimiento(None fechaNacimiento) {
        this.fechaNacimiento = fechaNacimiento;
    }
    public int getDoctorid() {
        return doctorID;
    }

    public void setDoctorid(int doctorID) {
        this.doctorID = doctorID;
    }
    public String getAppaterno() {
        return apPaterno;
    }

    public void setAppaterno(String apPaterno) {
        this.apPaterno = apPaterno;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getCodigodoctor() {
        return codigoDoctor;
    }

    public void setCodigodoctor(String codigoDoctor) {
        this.codigoDoctor = codigoDoctor;
    }
    public int getEspecialidadid() {
        return especialidadID;
    }

    public void setEspecialidadid(int especialidadID) {
        this.especialidadID = especialidadID;
    }
    public String getApmaterno() {
        return apMaterno;
    }

    public void setApmaterno(String apMaterno) {
        this.apMaterno = apMaterno;
    }
    public int getNrodocumento() {
        return nroDocumento;
    }

    public void setNrodocumento(int nroDocumento) {
        this.nroDocumento = nroDocumento;
    }
    public int getLoginid() {
        return loginID;
    }

    public void setLoginid(int loginID) {
        this.loginID = loginID;
    }

    public List<consulta> getConsultas() {
        return consultas;
    }

    public void addConsulta(Consulta consulta) {
        this.consultas.add(consulta);
    }

}