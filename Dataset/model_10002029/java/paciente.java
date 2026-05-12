





import java.util.List;
import java.util.ArrayList;

public class paciente  {

    private String codigoAsegurado;
    private String apPaterno;
    private String nombre;
    private int pacienteID;
    private String razonSocial;
    private int nroDocumento;
    private int aseguradoID;
    private String tipoSangre;
    private String apMaterno;
    private None fechaNacimiento;
    private None fechaAfiliacion;



    public paciente(
        String codigoAsegurado,        String apPaterno,        String nombre,        int pacienteID,        String razonSocial,        int nroDocumento,        int aseguradoID,        String tipoSangre,        String apMaterno,        None fechaNacimiento,        None fechaAfiliacion    ) {
        this.codigoAsegurado = codigoAsegurado;
        this.apPaterno = apPaterno;
        this.nombre = nombre;
        this.pacienteID = pacienteID;
        this.razonSocial = razonSocial;
        this.nroDocumento = nroDocumento;
        this.aseguradoID = aseguradoID;
        this.tipoSangre = tipoSangre;
        this.apMaterno = apMaterno;
        this.fechaNacimiento = fechaNacimiento;
        this.fechaAfiliacion = fechaAfiliacion;
    }


    public String getCodigoasegurado() {
        return codigoAsegurado;
    }

    public void setCodigoasegurado(String codigoAsegurado) {
        this.codigoAsegurado = codigoAsegurado;
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
    public int getPacienteid() {
        return pacienteID;
    }

    public void setPacienteid(int pacienteID) {
        this.pacienteID = pacienteID;
    }
    public String getRazonsocial() {
        return razonSocial;
    }

    public void setRazonsocial(String razonSocial) {
        this.razonSocial = razonSocial;
    }
    public int getNrodocumento() {
        return nroDocumento;
    }

    public void setNrodocumento(int nroDocumento) {
        this.nroDocumento = nroDocumento;
    }
    public int getAseguradoid() {
        return aseguradoID;
    }

    public void setAseguradoid(int aseguradoID) {
        this.aseguradoID = aseguradoID;
    }
    public String getTiposangre() {
        return tipoSangre;
    }

    public void setTiposangre(String tipoSangre) {
        this.tipoSangre = tipoSangre;
    }
    public String getApmaterno() {
        return apMaterno;
    }

    public void setApmaterno(String apMaterno) {
        this.apMaterno = apMaterno;
    }
    public None getFechanacimiento() {
        return fechaNacimiento;
    }

    public void setFechanacimiento(None fechaNacimiento) {
        this.fechaNacimiento = fechaNacimiento;
    }
    public None getFechaafiliacion() {
        return fechaAfiliacion;
    }

    public void setFechaafiliacion(None fechaAfiliacion) {
        this.fechaAfiliacion = fechaAfiliacion;
    }


}