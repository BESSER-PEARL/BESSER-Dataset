





import java.util.List;
import java.util.ArrayList;

public class caninos  {

    private String altura;
    private String raza;
    private String observaciones;
    private String nombre;
    private String peso;
    private String edad;





    private List<veterinaria> veterinarias;


    public caninos(
        String altura,        String raza,        String observaciones,        String nombre,        String peso,        String edad    ) {
        this.altura = altura;
        this.raza = raza;
        this.observaciones = observaciones;
        this.nombre = nombre;
        this.peso = peso;
        this.edad = edad;
        this.veterinarias = new ArrayList<>();
    }

    public caninos(
        String altura,        String raza,        String observaciones,        String nombre,        String peso,        String edad        ArrayList<veterinaria> veterinarias    ) {
        this.altura = altura;
        this.raza = raza;
        this.observaciones = observaciones;
        this.nombre = nombre;
        this.peso = peso;
        this.edad = edad;
        this.veterinarias = veterinarias;
    }

    public String getAltura() {
        return altura;
    }

    public void setAltura(String altura) {
        this.altura = altura;
    }
    public String getRaza() {
        return raza;
    }

    public void setRaza(String raza) {
        this.raza = raza;
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
    public String getPeso() {
        return peso;
    }

    public void setPeso(String peso) {
        this.peso = peso;
    }
    public String getEdad() {
        return edad;
    }

    public void setEdad(String edad) {
        this.edad = edad;
    }

    public List<veterinaria> getVeterinarias() {
        return veterinarias;
    }

    public void addVeterinaria(Veterinaria veterinaria) {
        this.veterinarias.add(veterinaria);
    }

}