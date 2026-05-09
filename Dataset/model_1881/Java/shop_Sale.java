





import java.util.List;
import java.util.ArrayList;

public class shop_Sale extends Valuable {

    private String description;





    private shop_Shop shop_shop;




    private List<shop_Employee> shop_employees;




    private shop_Employee shop_employee;




    private shop_Customer shop_customer;




    private shop_Customer shop_customer;


    public shop_Sale(
        String description    ) {
        super(
        );
        this.description = description;
        this.shop_employees = new ArrayList<>();
    }

    public shop_Sale(
        String description        ArrayList<shop_Employee> shop_employees    ) {
        this.description = description;
        this.shop_employees = shop_employees;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public shop_Shop getShop_shop() {
        return shop_shop;
    }

    public void setShop_shop(shop_Shop shop_shop) {
        this.shop_shop = shop_shop;
    }
    public List<shop_Employee> getShop_employees() {
        return shop_employees;
    }

    public void addShop_employee(Shop_employee shop_employee) {
        this.shop_employees.add(shop_employee);
    }
    public shop_Employee getShop_employee() {
        return shop_employee;
    }

    public void setShop_employee(shop_Employee shop_employee) {
        this.shop_employee = shop_employee;
    }
    public shop_Customer getShop_customer() {
        return shop_customer;
    }

    public void setShop_customer(shop_Customer shop_customer) {
        this.shop_customer = shop_customer;
    }
    public shop_Customer getShop_customer() {
        return shop_customer;
    }

    public void setShop_customer(shop_Customer shop_customer) {
        this.shop_customer = shop_customer;
    }

}