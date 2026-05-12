





import java.util.List;
import java.util.ArrayList;

public class Train  {

    private String type;
    private int trucks;



    public Train(
        String type,        int trucks    ) {
        this.type = type;
        this.trucks = trucks;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getTrucks() {
        return trucks;
    }

    public void setTrucks(int trucks) {
        this.trucks = trucks;
    }


}