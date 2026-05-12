





import java.util.List;
import java.util.ArrayList;

public class Online_pizza_ordering  {

    private float Price;
    private String Ingredients;
    private String pizza_type;





    private List<Customer> customers;




    private Admin admin;


    public Online_pizza_ordering(
        float Price,        String Ingredients,        String pizza_type    ) {
        this.Price = Price;
        this.Ingredients = Ingredients;
        this.pizza_type = pizza_type;
        this.customers = new ArrayList<>();
    }

    public Online_pizza_ordering(
        float Price,        String Ingredients,        String pizza_type        ArrayList<Customer> customers    ) {
        this.Price = Price;
        this.Ingredients = Ingredients;
        this.pizza_type = pizza_type;
        this.customers = customers;
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
    public String getPizza_type() {
        return pizza_type;
    }

    public void setPizza_type(String pizza_type) {
        this.pizza_type = pizza_type;
    }

    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }
    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }

}