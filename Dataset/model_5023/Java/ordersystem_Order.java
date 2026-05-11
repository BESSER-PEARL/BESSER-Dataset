





import java.util.List;
import java.util.ArrayList;

public class ordersystem_Order  {

    private String filledOn;
    private String placedOn;
    private String id;
    private boolean completed;



    public ordersystem_Order(
        String filledOn,        String placedOn,        String id,        boolean completed    ) {
        this.filledOn = filledOn;
        this.placedOn = placedOn;
        this.id = id;
        this.completed = completed;
    }


    public String getFilledon() {
        return filledOn;
    }

    public void setFilledon(String filledOn) {
        this.filledOn = filledOn;
    }
    public String getPlacedon() {
        return placedOn;
    }

    public void setPlacedon(String placedOn) {
        this.placedOn = placedOn;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getCompleted() {
        return completed;
    }

    public void setCompleted(boolean completed) {
        this.completed = completed;
    }


}