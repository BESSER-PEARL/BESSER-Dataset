





import java.util.List;
import java.util.ArrayList;

public class hockeyleague_Arena extends HockeyleagueObject {

    private int capacity;
    private String address;



    public hockeyleague_Arena(
        int capacity,        String address    ) {
        super(
        );
        this.capacity = capacity;
        this.address = address;
    }


    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}