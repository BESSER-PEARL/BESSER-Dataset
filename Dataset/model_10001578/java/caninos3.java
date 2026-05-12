





import java.util.List;
import java.util.ArrayList;

public class caninos3  {

    private String peso;
    private String raza;
    private String altura;
    private String edad;
    private String observaciones;
    private String nombre;





    private List<veterinaria3> veterinaria3s;


    public caninos3(
        String peso,        String raza,        String altura,        String edad,        String observaciones,        String nombre    ) {
        this.peso = peso;
        this.raza = raza;
        this.altura = altura;
        this.edad = edad;
        this.observaciones = observaciones;
        this.nombre = nombre;
        this.veterinaria3s = new ArrayList<>();
    }

    public caninos3(
        String peso,        String raza,        String altura,        String edad,        String observaciones,        String nombre        ArrayList<veterinaria3> veterinaria3s    ) {
        this.peso = peso;
        this.raza = raza;
        this.altura = altura;
        this.edad = edad;
        this.observaciones = observaciones;
        this.nombre = nombre;
        this.veterinaria3s = veterinaria3s;
    }

    public String getPeso() {
        return peso;
    }

    public void setPeso(String peso) {
        this.peso = peso;
    }
    public String getRaza() {
        return raza;
    }

    public void setRaza(String raza) {
        this.raza = raza;
    }
    public String getAltura() {
        return altura;
    }

    public void setAltura(String altura) {
        this.altura = altura;
    }
    public String getEdad() {
        return edad;
    }

    public void setEdad(String edad) {
        this.edad = edad;
    }
    public String getObservaciones() {
        return observaciones;
    }

    public void setObservaciones(String observaciones) {
        this.observaciones = observaciones;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public List<veterinaria3> getVeterinaria3s() {
        return veterinaria3s;
    }

    public void addVeterinaria3(Veterinaria3 veterinaria3) {
        this.veterinaria3s.add(veterinaria3);
    }

}