





import java.util.List;
import java.util.ArrayList;

public class Pedido  {

    private String Fecha;
    private String Numero;





    private Cliente cliente;


    public Pedido(
        String Fecha,        String Numero    ) {
        this.Fecha = Fecha;
        this.Numero = Numero;
    }


    public String getFecha() {
        return Fecha;
    }

    public void setFecha(String Fecha) {
        this.Fecha = Fecha;
    }
    public String getNumero() {
        return Numero;
    }

    public void setNumero(String Numero) {
        this.Numero = Numero;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

}