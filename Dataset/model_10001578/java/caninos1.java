





import java.util.List;
import java.util.ArrayList;

public class caninos1  {

    private String peso;
    private String altura;
    private String raza;
    private String edad;
    private String obsercaciones;
    private String nombre;





    private List<veterinaria1> veterinaria1s;


    public caninos1(
        String peso,        String altura,        String raza,        String edad,        String obsercaciones,        String nombre    ) {
        this.peso = peso;
        this.altura = altura;
        this.raza = raza;
        this.edad = edad;
        this.obsercaciones = obsercaciones;
        this.nombre = nombre;
        this.veterinaria1s = new ArrayList<>();
    }

    public caninos1(
        String peso,        String altura,        String raza,        String edad,        String obsercaciones,        String nombre        ArrayList<veterinaria1> veterinaria1s    ) {
        this.peso = peso;
        this.altura = altura;
        this.raza = raza;
        this.edad = edad;
        this.obsercaciones = obsercaciones;
        this.nombre = nombre;
        this.veterinaria1s = veterinaria1s;
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
    public String getObsercaciones() {
        return obsercaciones;
    }

    public void setObsercaciones(String obsercaciones) {
        this.obsercaciones = obsercaciones;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public List<veterinaria1> getVeterinaria1s() {
        return veterinaria1s;
    }

    public void addVeterinaria1(Veterinaria1 veterinaria1) {
        this.veterinaria1s.add(veterinaria1);
    }

}