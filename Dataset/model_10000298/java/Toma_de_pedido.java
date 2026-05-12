




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Toma_de_pedido  {

    private LocalDate Despacho;
    private String Tipo_de_elemnto;





    private Cliente cliente;




    private List<Pago> pagos;


    public Toma_de_pedido(
        LocalDate Despacho,        String Tipo_de_elemnto    ) {
        this.Despacho = Despacho;
        this.Tipo_de_elemnto = Tipo_de_elemnto;
        this.pagos = new ArrayList<>();
    }

    public Toma_de_pedido(
        LocalDate Despacho,        String Tipo_de_elemnto        ArrayList<Pago> pagos    ) {
        this.Despacho = Despacho;
        this.Tipo_de_elemnto = Tipo_de_elemnto;
        this.pagos = pagos;
    }

    public LocalDate getDespacho() {
        return Despacho;
    }

    public void setDespacho(LocalDate Despacho) {
        this.Despacho = Despacho;
    }
    public String getTipo_de_elemnto() {
        return Tipo_de_elemnto;
    }

    public void setTipo_de_elemnto(String Tipo_de_elemnto) {
        this.Tipo_de_elemnto = Tipo_de_elemnto;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }
    public List<Pago> getPagos() {
        return pagos;
    }

    public void addPago(Pago pago) {
        this.pagos.add(pago);
    }

}