





import java.util.List;
import java.util.ArrayList;

public class spot  {

    private String id;
    private int size;
    private None parkedVehicle;



    public spot(
        String id,        int size,        None parkedVehicle    ) {
        this.id = id;
        this.size = size;
        this.parkedVehicle = parkedVehicle;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public None getParkedvehicle() {
        return parkedVehicle;
    }

    public void setParkedvehicle(None parkedVehicle) {
        this.parkedVehicle = parkedVehicle;
    }


}