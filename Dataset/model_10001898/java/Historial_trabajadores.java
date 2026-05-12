





import java.util.List;
import java.util.ArrayList;

public class Historial_trabajadores  {

    private String TrabajoAntiguo;
    private String horasTrabajadas;
    private String codigo;





    private Trabajadores trabajadores;


    public Historial_trabajadores(
        String TrabajoAntiguo,        String horasTrabajadas,        String codigo    ) {
        this.TrabajoAntiguo = TrabajoAntiguo;
        this.horasTrabajadas = horasTrabajadas;
        this.codigo = codigo;
    }


    public String getTrabajoantiguo() {
        return TrabajoAntiguo;
    }

    public void setTrabajoantiguo(String TrabajoAntiguo) {
        this.TrabajoAntiguo = TrabajoAntiguo;
    }
    public String getHorastrabajadas() {
        return horasTrabajadas;
    }

    public void setHorastrabajadas(String horasTrabajadas) {
        this.horasTrabajadas = horasTrabajadas;
    }
    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public Trabajadores getTrabajadores() {
        return trabajadores;
    }

    public void setTrabajadores(Trabajadores trabajadores) {
        this.trabajadores = trabajadores;
    }

}