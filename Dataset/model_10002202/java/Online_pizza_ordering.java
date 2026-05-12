





import java.util.List;
import java.util.ArrayList;

public class Online_pizza_ordering  {

    private String pizza_type;
    private String Ingredients;
    private float Price;





    private List<Customer> customers;




    private Admin admin;


    public Online_pizza_ordering(
        String pizza_type,        String Ingredients,        float Price    ) {
        this.pizza_type = pizza_type;
        this.Ingredients = Ingredients;
        this.Price = Price;
        this.customers = new ArrayList<>();
    }

    public Online_pizza_ordering(
        String pizza_type,        String Ingredients,        float Price        ArrayList<Customer> customers    ) {
        this.pizza_type = pizza_type;
        this.Ingredients = Ingredients;
        this.Price = Price;
        this.customers = customers;
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
    public float getPrice() {
        return Price;
    }

    public void setPrice(float Price) {
        this.Price = Price;
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