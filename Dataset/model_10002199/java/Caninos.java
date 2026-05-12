





import java.util.List;
import java.util.ArrayList;

public class Caninos  {

    private String raza;
    private String nombre;
    private String edad;
    private String observaciones;
    private String altura;
    private String peso;





    private List<Empresa> empresas;




    private Empresa empresa;




    private List<Empresa> empresas;




    private List<Empresa> empresas;


    public Caninos(
        String raza,        String nombre,        String edad,        String observaciones,        String altura,        String peso    ) {
        this.raza = raza;
        this.nombre = nombre;
        this.edad = edad;
        this.observaciones = observaciones;
        this.altura = altura;
        this.peso = peso;
        this.empresas = new ArrayList<>();
        this.empresas = new ArrayList<>();
        this.empresas = new ArrayList<>();
    }

    public Caninos(
        String raza,        String nombre,        String edad,        String observaciones,        String altura,        String peso        ArrayList<Empresa> empresas,        ArrayList<Empresa> empresas,        ArrayList<Empresa> empresas    ) {
        this.raza = raza;
        this.nombre = nombre;
        this.edad = edad;
        this.observaciones = observaciones;
        this.altura = altura;
        this.peso = peso;
        this.empresas = empresas;
        this.empresas = empresas;
        this.empresas = empresas;
    }

    public String getRaza() {
        return raza;
    }

    public void setRaza(String raza) {
        this.raza = raza;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
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

    public List<Empresa> getEmpresas() {
        return empresas;
    }

    public void addEmpresa(Empresa empresa) {
        this.empresas.add(empresa);
    }
    public Empresa getEmpresa() {
        return empresa;
    }

    public void setEmpresa(Empresa empresa) {
        this.empresa = empresa;
    }
    public List<Empresa> getEmpresas() {
        return empresas;
    }

    public void addEmpresa(Empresa empresa) {
        this.empresas.add(empresa);
    }
    public List<Empresa> getEmpresas() {
        return empresas;
    }

    public void addEmpresa(Empresa empresa) {
        this.empresas.add(empresa);
    }

}