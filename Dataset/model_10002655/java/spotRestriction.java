





import java.util.List;
import java.util.ArrayList;

public class spotRestriction  {

    private int size;
    private None spotType;



    public spotRestriction(
        int size,        None spotType    ) {
        this.size = size;
        this.spotType = spotType;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public None getSpottype() {
        return spotType;
    }

    public void setSpottype(None spotType) {
        this.spotType = spotType;
    }


}