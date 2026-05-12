





import java.util.List;
import java.util.ArrayList;

public class Event  {

    private float created_at;
    private String entity;



    public Event(
        float created_at,        String entity    ) {
        this.created_at = created_at;
        this.entity = entity;
    }


    public float getCreated_at() {
        return created_at;
    }

    public void setCreated_at(float created_at) {
        this.created_at = created_at;
    }
    public String getEntity() {
        return entity;
    }

    public void setEntity(String entity) {
        this.entity = entity;
    }


}