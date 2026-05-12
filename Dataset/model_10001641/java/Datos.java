





import java.util.List;
import java.util.ArrayList;

public class Datos  {

    private int Edad;
    private String peso;
    private String altura;
    private String nombre;
    private String raza;
    private String observacion;





    private List<Veterinario> veterinarios;


    public Datos(
        int Edad,        String peso,        String altura,        String nombre,        String raza,        String observacion    ) {
        this.Edad = Edad;
        this.peso = peso;
        this.altura = altura;
        this.nombre = nombre;
        this.raza = raza;
        this.observacion = observacion;
        this.veterinarios = new ArrayList<>();
    }

    public Datos(
        int Edad,        String peso,        String altura,        String nombre,        String raza,        String observacion        ArrayList<Veterinario> veterinarios    ) {
        this.Edad = Edad;
        this.peso = peso;
        this.altura = altura;
        this.nombre = nombre;
        this.raza = raza;
        this.observacion = observacion;
        this.veterinarios = veterinarios;
    }

    public int getEdad() {
        return Edad;
    }

    public void setEdad(int Edad) {
        this.Edad = Edad;
    }
    public String getPeso() {
        return peso;
    }

    public void setPeso(String peso) {
        this.peso = peso;
    }
    public String getAltura() {
        return altura;
    }

    public void setAltura(String altura) {
        this.altura = altura;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getRaza() {
        return raza;
    }

    public void setRaza(String raza) {
        this.raza = raza;
    }
    public String getObservacion() {
        return observacion;
    }

    public void setObservacion(String observacion) {
        this.observacion = observacion;
    }

    public List<Veterinario> getVeterinarios() {
        return veterinarios;
    }

    public void addVeterinario(Veterinario veterinario) {
        this.veterinarios.add(veterinario);
    }

}