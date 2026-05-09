





import java.util.List;
import java.util.ArrayList;

public class shop_Shop  {






    private List<shop_Employee> shop_employees;




    private List<shop_Customer> shop_customers;


    public shop_Shop(
    ) {
        this.shop_employees = new ArrayList<>();
        this.shop_customers = new ArrayList<>();
    }

    public shop_Shop(
        ArrayList<shop_Employee> shop_employees,        ArrayList<shop_Customer> shop_customers    ) {
        this.shop_employees = shop_employees;
        this.shop_customers = shop_customers;
    }


    public List<shop_Employee> getShop_employees() {
        return shop_employees;
    }

    public void addShop_employee(Shop_employee shop_employee) {
        this.shop_employees.add(shop_employee);
    }
    public List<shop_Customer> getShop_customers() {
        return shop_customers;
    }

    public void addShop_customer(Shop_customer shop_customer) {
        this.shop_customers.add(shop_customer);
    }

}