





import java.util.List;
import java.util.ArrayList;

public class caninos2  {

    private String raza;
    private String edad;
    private String observaciones;
    private String nombre;
    private String altura;
    private String peso;





    private List<veterinaria2> veterinaria2s;


    public caninos2(
        String raza,        String edad,        String observaciones,        String nombre,        String altura,        String peso    ) {
        this.raza = raza;
        this.edad = edad;
        this.observaciones = observaciones;
        this.nombre = nombre;
        this.altura = altura;
        this.peso = peso;
        this.veterinaria2s = new ArrayList<>();
    }

    public caninos2(
        String raza,        String edad,        String observaciones,        String nombre,        String altura,        String peso        ArrayList<veterinaria2> veterinaria2s    ) {
        this.raza = raza;
        this.edad = edad;
        this.observaciones = observaciones;
        this.nombre = nombre;
        this.altura = altura;
        this.peso = peso;
        this.veterinaria2s = veterinaria2s;
    }

    public String getRaza() {
        return raza;
    }

    public void setRaza(String raza) {
        this.raza = raza;
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
    public String getAltura() {
        return altura;
    }

    public void setAltura(String altura) {
        this.altura = altura;
    }
    public String getPeso() {
        return peso;
    }

    public void setPeso(String peso) {
        this.peso = peso;
    }

    public List<veterinaria2> getVeterinaria2s() {
        return veterinaria2s;
    }

    public void addVeterinaria2(Veterinaria2 veterinaria2) {
        this.veterinaria2s.add(veterinaria2);
    }

}