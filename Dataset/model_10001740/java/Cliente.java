





import java.util.List;
import java.util.ArrayList;

public class Cliente  {

    private String numeroDeCliente;
    private String listaMascotas;
    private String nombre;



    public Cliente(
        String numeroDeCliente,        String listaMascotas,        String nombre    ) {
        this.numeroDeCliente = numeroDeCliente;
        this.listaMascotas = listaMascotas;
        this.nombre = nombre;
    }


    public String getNumerodecliente() {
        return numeroDeCliente;
    }

    public void setNumerodecliente(String numeroDeCliente) {
        this.numeroDeCliente = numeroDeCliente;
    }
    public String getListamascotas() {
        return listaMascotas;
    }

    public void setListamascotas(String listaMascotas) {
        this.listaMascotas = listaMascotas;
    }
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }


}