





import java.util.List;
import java.util.ArrayList;

public class Classes_Bookables_Bookable  {

    private String description;
    private String id;
    private float baseprice;



    public Classes_Bookables_Bookable(
        String description,        String id,        float baseprice    ) {
        this.description = description;
        this.id = id;
        this.baseprice = baseprice;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public float getBaseprice() {
        return baseprice;
    }

    public void setBaseprice(float baseprice) {
        this.baseprice = baseprice;
    }


}