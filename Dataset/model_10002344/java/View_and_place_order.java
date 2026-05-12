





import java.util.List;
import java.util.ArrayList;

public class View_and_place_order  {

    private None place_order;
    private None order_view;



    public View_and_place_order(
        None place_order,        None order_view    ) {
        this.place_order = place_order;
        this.order_view = order_view;
    }


    public None getPlace_order() {
        return place_order;
    }

    public void setPlace_order(None place_order) {
        this.place_order = place_order;
    }
    public None getOrder_view() {
        return order_view;
    }

    public void setOrder_view(None order_view) {
        this.order_view = order_view;
    }


}