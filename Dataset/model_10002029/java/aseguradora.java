





import java.util.List;
import java.util.ArrayList;

public class aseguradora  {

    private String nombre;
    private int tipoSeguroID;
    private int aseguradoraID;





    private List<paciente> pacientes;


    public aseguradora(
        String nombre,        int tipoSeguroID,        int aseguradoraID    ) {
        this.nombre = nombre;
        this.tipoSeguroID = tipoSeguroID;
        this.aseguradoraID = aseguradoraID;
        this.pacientes = new ArrayList<>();
    }

    public aseguradora(
        String nombre,        int tipoSeguroID,        int aseguradoraID        ArrayList<paciente> pacientes    ) {
        this.nombre = nombre;
        this.tipoSeguroID = tipoSeguroID;
        this.aseguradoraID = aseguradoraID;
        this.pacientes = pacientes;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public int getTiposeguroid() {
        return tipoSeguroID;
    }

    public void setTiposeguroid(int tipoSeguroID) {
        this.tipoSeguroID = tipoSeguroID;
    }
    public int getAseguradoraid() {
        return aseguradoraID;
    }

    public void setAseguradoraid(int aseguradoraID) {
        this.aseguradoraID = aseguradoraID;
    }

    public List<paciente> getPacientes() {
        return pacientes;
    }

    public void addPaciente(Paciente paciente) {
        this.pacientes.add(paciente);
    }

}