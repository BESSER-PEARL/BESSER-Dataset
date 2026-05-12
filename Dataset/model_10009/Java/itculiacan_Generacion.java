




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class itculiacan_Generacion  {

    private LocalDate fechaFin;
    private LocalDate fechaInicio;





    private List<itculiacan_Alumno> itculiacan_alumnos;




    private itculiacan_Alumno itculiacan_alumno;


    public itculiacan_Generacion(
        LocalDate fechaFin,        LocalDate fechaInicio    ) {
        this.fechaFin = fechaFin;
        this.fechaInicio = fechaInicio;
        this.itculiacan_alumnos = new ArrayList<>();
    }

    public itculiacan_Generacion(
        LocalDate fechaFin,        LocalDate fechaInicio        ArrayList<itculiacan_Alumno> itculiacan_alumnos    ) {
        this.fechaFin = fechaFin;
        this.fechaInicio = fechaInicio;
        this.itculiacan_alumnos = itculiacan_alumnos;
    }

    public LocalDate getFechafin() {
        return fechaFin;
    }

    public void setFechafin(LocalDate fechaFin) {
        this.fechaFin = fechaFin;
    }
    public LocalDate getFechainicio() {
        return fechaInicio;
    }

    public void setFechainicio(LocalDate fechaInicio) {
        this.fechaInicio = fechaInicio;
    }

    public List<itculiacan_Alumno> getItculiacan_alumnos() {
        return itculiacan_alumnos;
    }

    public void addItculiacan_alumno(Itculiacan_alumno itculiacan_alumno) {
        this.itculiacan_alumnos.add(itculiacan_alumno);
    }
    public itculiacan_Alumno getItculiacan_alumno() {
        return itculiacan_alumno;
    }

    public void setItculiacan_alumno(itculiacan_Alumno itculiacan_alumno) {
        this.itculiacan_alumno = itculiacan_alumno;
    }

}