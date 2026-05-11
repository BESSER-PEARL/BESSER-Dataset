





import java.util.List;
import java.util.ArrayList;

public class accounting_Project extends NamedElement {






    private List<accounting_Order> accounting_orders;




    private accounting_Order accounting_order;


    public accounting_Project(
    ) {
        super(
        );
        this.accounting_orders = new ArrayList<>();
    }

    public accounting_Project(
        ArrayList<accounting_Order> accounting_orders    ) {
        this.accounting_orders = accounting_orders;
    }


    public List<accounting_Order> getAccounting_orders() {
        return accounting_orders;
    }

    public void addAccounting_order(Accounting_order accounting_order) {
        this.accounting_orders.add(accounting_order);
    }
    public accounting_Order getAccounting_order() {
        return accounting_order;
    }

    public void setAccounting_order(accounting_Order accounting_order) {
        this.accounting_order = accounting_order;
    }

}