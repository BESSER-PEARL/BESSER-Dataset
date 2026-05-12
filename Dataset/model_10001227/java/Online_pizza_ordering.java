





import java.util.List;
import java.util.ArrayList;

public class Online_pizza_ordering  {

    private float Price;
    private String pizza_type;
    private String Ingredients;





    private Admin admin;




    private List<Customer> customers;


    public Online_pizza_ordering(
        float Price,        String pizza_type,        String Ingredients    ) {
        this.Price = Price;
        this.pizza_type = pizza_type;
        this.Ingredients = Ingredients;
        this.customers = new ArrayList<>();
    }

    public Online_pizza_ordering(
        float Price,        String pizza_type,        String Ingredients        ArrayList<Customer> customers    ) {
        this.Price = Price;
        this.pizza_type = pizza_type;
        this.Ingredients = Ingredients;
        this.customers = customers;
    }

    public float getPrice() {
        return Price;
    }

    public void setPrice(float Price) {
        this.Price = Price;
    }
    public String getPizza_type() {
        return pizza_type;
    }

    public void setPizza_type(String pizza_type) {
        this.pizza_type = pizza_type;
    }
    public String getIngredients() {
        return Ingredients;
    }

    public void setIngredients(String Ingredients) {
        this.Ingredients = Ingredients;
    }

    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }
    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }

}