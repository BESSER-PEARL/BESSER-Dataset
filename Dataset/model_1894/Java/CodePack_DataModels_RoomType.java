





import java.util.List;
import java.util.ArrayList;

public class CodePack_DataModels_RoomType  {

    private int max_guests;
    private String description;
    private float rate;
    private String typename;



    public CodePack_DataModels_RoomType(
        int max_guests,        String description,        float rate,        String typename    ) {
        this.max_guests = max_guests;
        this.description = description;
        this.rate = rate;
        this.typename = typename;
    }


    public int getMax_guests() {
        return max_guests;
    }

    public void setMax_guests(int max_guests) {
        this.max_guests = max_guests;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public float getRate() {
        return rate;
    }

    public void setRate(float rate) {
        this.rate = rate;
    }
    public String getTypename() {
        return typename;
    }

    public void setTypename(String typename) {
        this.typename = typename;
    }


}