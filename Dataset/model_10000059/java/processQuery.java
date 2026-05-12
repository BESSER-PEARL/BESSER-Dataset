





import java.util.List;
import java.util.ArrayList;

public class processQuery  {






    private Table table;




    private OrderController ordercontroller;




    private AdminController admincontroller;




    private BookingController bookingcontroller;


    public processQuery(
    ) {
    }



    public Table getTable() {
        return table;
    }

    public void setTable(Table table) {
        this.table = table;
    }
    public OrderController getOrdercontroller() {
        return ordercontroller;
    }

    public void setOrdercontroller(OrderController ordercontroller) {
        this.ordercontroller = ordercontroller;
    }
    public AdminController getAdmincontroller() {
        return admincontroller;
    }

    public void setAdmincontroller(AdminController admincontroller) {
        this.admincontroller = admincontroller;
    }
    public BookingController getBookingcontroller() {
        return bookingcontroller;
    }

    public void setBookingcontroller(BookingController bookingcontroller) {
        this.bookingcontroller = bookingcontroller;
    }

}