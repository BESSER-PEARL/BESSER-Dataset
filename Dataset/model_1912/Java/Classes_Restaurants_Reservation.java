




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Classes_Restaurants_Reservation  {

    private LocalDate from_;
    private LocalDate to;
    private String reservedBy;
    private String id;





    private List<RestaurantTable> restauranttables;


    public Classes_Restaurants_Reservation(
        LocalDate from_,        LocalDate to,        String reservedBy,        String id    ) {
        this.from_ = from_;
        this.to = to;
        this.reservedBy = reservedBy;
        this.id = id;
        this.restauranttables = new ArrayList<>();
    }

    public Classes_Restaurants_Reservation(
        LocalDate from_,        LocalDate to,        String reservedBy,        String id        ArrayList<RestaurantTable> restauranttables    ) {
        this.from_ = from_;
        this.to = to;
        this.reservedBy = reservedBy;
        this.id = id;
        this.restauranttables = restauranttables;
    }

    public LocalDate getFrom_() {
        return from_;
    }

    public void setFrom_(LocalDate from_) {
        this.from_ = from_;
    }
    public LocalDate getTo() {
        return to;
    }

    public void setTo(LocalDate to) {
        this.to = to;
    }
    public String getReservedby() {
        return reservedBy;
    }

    public void setReservedby(String reservedBy) {
        this.reservedBy = reservedBy;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<RestaurantTable> getRestauranttables() {
        return restauranttables;
    }

    public void addRestauranttable(Restauranttable restauranttable) {
        this.restauranttables.add(restauranttable);
    }

}