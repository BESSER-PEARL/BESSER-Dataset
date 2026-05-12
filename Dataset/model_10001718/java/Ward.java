





import java.util.List;
import java.util.ArrayList;

public class Ward  {

    private int capacity;
    private String name;





    private Hospital hospital;


    public Ward(
        int capacity,        String name    ) {
        this.capacity = capacity;
        this.name = name;
    }


    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Hospital getHospital() {
        return hospital;
    }

    public void setHospital(Hospital hospital) {
        this.hospital = hospital;
    }

}