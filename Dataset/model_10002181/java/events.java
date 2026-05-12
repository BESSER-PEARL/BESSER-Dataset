





import java.util.List;
import java.util.ArrayList;

public class events  {

    private String attribute;
    private String catering_location;
    private String duration;
    private String get_employee_name;





    private dayplan dayplan;




    private kitchen_worker kitchen_worker;




    private List<order> orders;




    private food_dish food_dish;




    private events events;




    private List<food_dish> food_dishs;




    private List<food_dish> food_dishs;




    private List<kitchen_worker> kitchen_workers;




    private List<Component> components;




    private Component component;


    public events(
        String attribute,        String catering_location,        String duration,        String get_employee_name    ) {
        this.attribute = attribute;
        this.catering_location = catering_location;
        this.duration = duration;
        this.get_employee_name = get_employee_name;
        this.orders = new ArrayList<>();
        this.food_dishs = new ArrayList<>();
        this.food_dishs = new ArrayList<>();
        this.kitchen_workers = new ArrayList<>();
        this.components = new ArrayList<>();
    }

    public events(
        String attribute,        String catering_location,        String duration,        String get_employee_name        ArrayList<order> orders,        ArrayList<food_dish> food_dishs,        ArrayList<food_dish> food_dishs,        ArrayList<kitchen_worker> kitchen_workers,        ArrayList<Component> components    ) {
        this.attribute = attribute;
        this.catering_location = catering_location;
        this.duration = duration;
        this.get_employee_name = get_employee_name;
        this.orders = orders;
        this.food_dishs = food_dishs;
        this.food_dishs = food_dishs;
        this.kitchen_workers = kitchen_workers;
        this.components = components;
    }

    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getCatering_location() {
        return catering_location;
    }

    public void setCatering_location(String catering_location) {
        this.catering_location = catering_location;
    }
    public String getDuration() {
        return duration;
    }

    public void setDuration(String duration) {
        this.duration = duration;
    }
    public String getGet_employee_name() {
        return get_employee_name;
    }

    public void setGet_employee_name(String get_employee_name) {
        this.get_employee_name = get_employee_name;
    }

    public dayplan getDayplan() {
        return dayplan;
    }

    public void setDayplan(dayplan dayplan) {
        this.dayplan = dayplan;
    }
    public kitchen_worker getKitchen_worker() {
        return kitchen_worker;
    }

    public void setKitchen_worker(kitchen_worker kitchen_worker) {
        this.kitchen_worker = kitchen_worker;
    }
    public List<order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }
    public food_dish getFood_dish() {
        return food_dish;
    }

    public void setFood_dish(food_dish food_dish) {
        this.food_dish = food_dish;
    }
    public events getEvents() {
        return events;
    }

    public void setEvents(events events) {
        this.events = events;
    }
    public List<food_dish> getFood_dishs() {
        return food_dishs;
    }

    public void addFood_dish(Food_dish food_dish) {
        this.food_dishs.add(food_dish);
    }
    public List<food_dish> getFood_dishs() {
        return food_dishs;
    }

    public void addFood_dish(Food_dish food_dish) {
        this.food_dishs.add(food_dish);
    }
    public List<kitchen_worker> getKitchen_workers() {
        return kitchen_workers;
    }

    public void addKitchen_worker(Kitchen_worker kitchen_worker) {
        this.kitchen_workers.add(kitchen_worker);
    }
    public List<Component> getComponents() {
        return components;
    }

    public void addComponent(Component component) {
        this.components.add(component);
    }
    public Component getComponent() {
        return component;
    }

    public void setComponent(Component component) {
        this.component = component;
    }

}