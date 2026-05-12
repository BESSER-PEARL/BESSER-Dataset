





import java.util.List;
import java.util.ArrayList;

public class EventsProductGroup  {

    private int id;
    private None Event;
    private None ProductGroup;





    private ProductGroup productgroup;




    private Events events;


    public EventsProductGroup(
        int id,        None Event,        None ProductGroup    ) {
        this.id = id;
        this.Event = Event;
        this.ProductGroup = ProductGroup;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public None getEvent() {
        return Event;
    }

    public void setEvent(None Event) {
        this.Event = Event;
    }
    public None getProductgroup() {
        return ProductGroup;
    }

    public void setProductgroup(None ProductGroup) {
        this.ProductGroup = ProductGroup;
    }

    public ProductGroup getProductgroup() {
        return productgroup;
    }

    public void setProductgroup(ProductGroup productgroup) {
        this.productgroup = productgroup;
    }
    public Events getEvents() {
        return events;
    }

    public void setEvents(Events events) {
        this.events = events;
    }

}