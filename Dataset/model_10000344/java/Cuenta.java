




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Cuenta  {

    private boolean isClosed;
    private LocalDate closed;
    private LocalDate open;
    private String billingAddress;





    private Vendedor vendedor;




    private Venta venta;




    private List<Pago> pagos;


    public Cuenta(
        boolean isClosed,        LocalDate closed,        LocalDate open,        String billingAddress    ) {
        this.isClosed = isClosed;
        this.closed = closed;
        this.open = open;
        this.billingAddress = billingAddress;
        this.pagos = new ArrayList<>();
    }

    public Cuenta(
        boolean isClosed,        LocalDate closed,        LocalDate open,        String billingAddress        ArrayList<Pago> pagos    ) {
        this.isClosed = isClosed;
        this.closed = closed;
        this.open = open;
        this.billingAddress = billingAddress;
        this.pagos = pagos;
    }

    public boolean getIsclosed() {
        return isClosed;
    }

    public void setIsclosed(boolean isClosed) {
        this.isClosed = isClosed;
    }
    public LocalDate getClosed() {
        return closed;
    }

    public void setClosed(LocalDate closed) {
        this.closed = closed;
    }
    public LocalDate getOpen() {
        return open;
    }

    public void setOpen(LocalDate open) {
        this.open = open;
    }
    public String getBillingaddress() {
        return billingAddress;
    }

    public void setBillingaddress(String billingAddress) {
        this.billingAddress = billingAddress;
    }

    public Vendedor getVendedor() {
        return vendedor;
    }

    public void setVendedor(Vendedor vendedor) {
        this.vendedor = vendedor;
    }
    public Venta getVenta() {
        return venta;
    }

    public void setVenta(Venta venta) {
        this.venta = venta;
    }
    public List<Pago> getPagos() {
        return pagos;
    }

    public void addPago(Pago pago) {
        this.pagos.add(pago);
    }

}