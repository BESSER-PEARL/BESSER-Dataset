





import java.util.List;
import java.util.ArrayList;

public class spotRestriction  {

    private None spotType;
    private int size;



    public spotRestriction(
        None spotType,        int size    ) {
        this.spotType = spotType;
        this.size = size;
    }


    public None getSpottype() {
        return spotType;
    }

    public void setSpottype(None spotType) {
        this.spotType = spotType;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }


}