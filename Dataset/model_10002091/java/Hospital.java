





import java.util.List;
import java.util.ArrayList;

public class Hospital  {

    private String name;
    private int totalwards;



    public Hospital(
        String name,        int totalwards    ) {
        this.name = name;
        this.totalwards = totalwards;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getTotalwards() {
        return totalwards;
    }

    public void setTotalwards(int totalwards) {
        this.totalwards = totalwards;
    }


}