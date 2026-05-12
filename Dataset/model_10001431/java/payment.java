





import java.util.List;
import java.util.ArrayList;

public class payment  {

    private int tableno;
    private String name;





    private customer customer;




    private order order;


    public payment(
        int tableno,        String name    ) {
        this.tableno = tableno;
        this.name = name;
    }


    public int getTableno() {
        return tableno;
    }

    public void setTableno(int tableno) {
        this.tableno = tableno;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public customer getCustomer() {
        return customer;
    }

    public void setCustomer(customer customer) {
        this.customer = customer;
    }
    public order getOrder() {
        return order;
    }

    public void setOrder(order order) {
        this.order = order;
    }

}