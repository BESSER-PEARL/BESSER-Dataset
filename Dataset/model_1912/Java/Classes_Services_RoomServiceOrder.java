




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Classes_Services_RoomServiceOrder  {

    private String id;
    private String items;
    private String bill;
    private LocalDate deliveryDate;
    private String bookable;
    private String isDelivered;





    private List<Service> services;


    public Classes_Services_RoomServiceOrder(
        String id,        String items,        String bill,        LocalDate deliveryDate,        String bookable,        String isDelivered    ) {
        this.id = id;
        this.items = items;
        this.bill = bill;
        this.deliveryDate = deliveryDate;
        this.bookable = bookable;
        this.isDelivered = isDelivered;
        this.services = new ArrayList<>();
    }

    public Classes_Services_RoomServiceOrder(
        String id,        String items,        String bill,        LocalDate deliveryDate,        String bookable,        String isDelivered        ArrayList<Service> services    ) {
        this.id = id;
        this.items = items;
        this.bill = bill;
        this.deliveryDate = deliveryDate;
        this.bookable = bookable;
        this.isDelivered = isDelivered;
        this.services = services;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getItems() {
        return items;
    }

    public void setItems(String items) {
        this.items = items;
    }
    public String getBill() {
        return bill;
    }

    public void setBill(String bill) {
        this.bill = bill;
    }
    public LocalDate getDeliverydate() {
        return deliveryDate;
    }

    public void setDeliverydate(LocalDate deliveryDate) {
        this.deliveryDate = deliveryDate;
    }
    public String getBookable() {
        return bookable;
    }

    public void setBookable(String bookable) {
        this.bookable = bookable;
    }
    public String getIsdelivered() {
        return isDelivered;
    }

    public void setIsdelivered(String isDelivered) {
        this.isDelivered = isDelivered;
    }

    public List<Service> getServices() {
        return services;
    }

    public void addService(Service service) {
        this.services.add(service);
    }

}