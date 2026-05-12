





import java.util.List;
import java.util.ArrayList;

public class consulta  {

    private int consultaID;
    private int empleadoID;
    private None fechaConsulta;
    private int doctorID;
    private int pacienteID;





    private paciente paciente;


    public consulta(
        int consultaID,        int empleadoID,        None fechaConsulta,        int doctorID,        int pacienteID    ) {
        this.consultaID = consultaID;
        this.empleadoID = empleadoID;
        this.fechaConsulta = fechaConsulta;
        this.doctorID = doctorID;
        this.pacienteID = pacienteID;
    }


    public int getConsultaid() {
        return consultaID;
    }

    public void setConsultaid(int consultaID) {
        this.consultaID = consultaID;
    }
    public int getEmpleadoid() {
        return empleadoID;
    }

    public void setEmpleadoid(int empleadoID) {
        this.empleadoID = empleadoID;
    }
    public None getFechaconsulta() {
        return fechaConsulta;
    }

    public void setFechaconsulta(None fechaConsulta) {
        this.fechaConsulta = fechaConsulta;
    }
    public int getDoctorid() {
        return doctorID;
    }

    public void setDoctorid(int doctorID) {
        this.doctorID = doctorID;
    }
    public int getPacienteid() {
        return pacienteID;
    }

    public void setPacienteid(int pacienteID) {
        this.pacienteID = pacienteID;
    }

    public paciente getPaciente() {
        return paciente;
    }

    public void setPaciente(paciente paciente) {
        this.paciente = paciente;
    }

}