




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class cont  {

    private LocalDate open;
    private String billingAddress;
    private boolean isClosed;
    private LocalDate closed;





    private client client;




    private Cosul_de_cumparaturi cosul_de_cumparaturi;




    private List<Plata> platas;


    public cont(
        LocalDate open,        String billingAddress,        boolean isClosed,        LocalDate closed    ) {
        this.open = open;
        this.billingAddress = billingAddress;
        this.isClosed = isClosed;
        this.closed = closed;
        this.platas = new ArrayList<>();
    }

    public cont(
        LocalDate open,        String billingAddress,        boolean isClosed,        LocalDate closed        ArrayList<Plata> platas    ) {
        this.open = open;
        this.billingAddress = billingAddress;
        this.isClosed = isClosed;
        this.closed = closed;
        this.platas = platas;
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

    public client getClient() {
        return client;
    }

    public void setClient(client client) {
        this.client = client;
    }
    public Cosul_de_cumparaturi getCosul_de_cumparaturi() {
        return cosul_de_cumparaturi;
    }

    public void setCosul_de_cumparaturi(Cosul_de_cumparaturi cosul_de_cumparaturi) {
        this.cosul_de_cumparaturi = cosul_de_cumparaturi;
    }
    public List<Plata> getPlatas() {
        return platas;
    }

    public void addPlata(Plata plata) {
        this.platas.add(plata);
    }

}