





import java.util.List;
import java.util.ArrayList;

public class Online_pizza_ordering  {

    private String pizza_type;
    private float Price;
    private String Ingredients;





    private Admin admin;




    private List<Customer> customers;


    public Online_pizza_ordering(
        String pizza_type,        float Price,        String Ingredients    ) {
        this.pizza_type = pizza_type;
        this.Price = Price;
        this.Ingredients = Ingredients;
        this.customers = new ArrayList<>();
    }

    public Online_pizza_ordering(
        String pizza_type,        float Price,        String Ingredients        ArrayList<Customer> customers    ) {
        this.pizza_type = pizza_type;
        this.Price = Price;
        this.Ingredients = Ingredients;
        this.customers = customers;
    }

    public String getPizza_type() {
        return pizza_type;
    }

    public void setPizza_type(String pizza_type) {
        this.pizza_type = pizza_type;
    }
    public float getPrice() {
        return Price;
    }

    public void setPrice(float Price) {
        this.Price = Price;
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