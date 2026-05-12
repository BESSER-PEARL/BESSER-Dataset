





import java.util.List;
import java.util.ArrayList;

public class Inventory  {

    private String Products;
    private String Services;





    private Online_Portal online_portal;




    private List<Terminal> terminals;




    private Store store;


    public Inventory(
        String Products,        String Services    ) {
        this.Products = Products;
        this.Services = Services;
        this.terminals = new ArrayList<>();
    }

    public Inventory(
        String Products,        String Services        ArrayList<Terminal> terminals    ) {
        this.Products = Products;
        this.Services = Services;
        this.terminals = terminals;
    }

    public String getProducts() {
        return Products;
    }

    public void setProducts(String Products) {
        this.Products = Products;
    }
    public String getServices() {
        return Services;
    }

    public void setServices(String Services) {
        this.Services = Services;
    }

    public Online_Portal getOnline_portal() {
        return online_portal;
    }

    public void setOnline_portal(Online_Portal online_portal) {
        this.online_portal = online_portal;
    }
    public List<Terminal> getTerminals() {
        return terminals;
    }

    public void addTerminal(Terminal terminal) {
        this.terminals.add(terminal);
    }
    public Store getStore() {
        return store;
    }

    public void setStore(Store store) {
        this.store = store;
    }

}