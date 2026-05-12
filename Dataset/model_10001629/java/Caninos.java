





import java.util.List;
import java.util.ArrayList;

public class Caninos  {

    private String raza;
    private String altura;
    private String nombre;
    private String observaciones;
    private String edad;
    private String peso;





    private List<Empresa> empresas;


    public Caninos(
        String raza,        String altura,        String nombre,        String observaciones,        String edad,        String peso    ) {
        this.raza = raza;
        this.altura = altura;
        this.nombre = nombre;
        this.observaciones = observaciones;
        this.edad = edad;
        this.peso = peso;
        this.empresas = new ArrayList<>();
    }

    public Caninos(
        String raza,        String altura,        String nombre,        String observaciones,        String edad,        String peso        ArrayList<Empresa> empresas    ) {
        this.raza = raza;
        this.altura = altura;
        this.nombre = nombre;
        this.observaciones = observaciones;
        this.edad = edad;
        this.peso = peso;
        this.empresas = empresas;
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
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getObservaciones() {
        return observaciones;
    }

    public void setObservaciones(String observaciones) {
        this.observaciones = observaciones;
    }
    public String getEdad() {
        return edad;
    }

    public void setEdad(String edad) {
        this.edad = edad;
    }
    public String getPeso() {
        return peso;
    }

    public void setPeso(String peso) {
        this.peso = peso;
    }

    public List<Empresa> getEmpresas() {
        return empresas;
    }

    public void addEmpresa(Empresa empresa) {
        this.empresas.add(empresa);
    }

}