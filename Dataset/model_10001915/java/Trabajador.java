





import java.util.List;
import java.util.ArrayList;

public class Trabajador  {

    private int HrsTrabajadasMes;
    private String nombre;
    private int DNI;
    private int Sueldo;



    public Trabajador(
        int HrsTrabajadasMes,        String nombre,        int DNI,        int Sueldo    ) {
        this.HrsTrabajadasMes = HrsTrabajadasMes;
        this.nombre = nombre;
        this.DNI = DNI;
        this.Sueldo = Sueldo;
    }


    public int getHrstrabajadasmes() {
        return HrsTrabajadasMes;
    }

    public void setHrstrabajadasmes(int HrsTrabajadasMes) {
        this.HrsTrabajadasMes = HrsTrabajadasMes;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public int getDni() {
        return DNI;
    }

    public void setDni(int DNI) {
        this.DNI = DNI;
    }
    public int getSueldo() {
        return Sueldo;
    }

    public void setSueldo(int Sueldo) {
        this.Sueldo = Sueldo;
    }


}