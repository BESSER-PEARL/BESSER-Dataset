





import java.util.List;
import java.util.ArrayList;

public class scheduleOfCourse_CourseLoad  {

    private int totalQuantity;
    private int unitQuantity;
    private String type;



    public scheduleOfCourse_CourseLoad(
        int totalQuantity,        int unitQuantity,        String type    ) {
        this.totalQuantity = totalQuantity;
        this.unitQuantity = unitQuantity;
        this.type = type;
    }


    public int getTotalquantity() {
        return totalQuantity;
    }

    public void setTotalquantity(int totalQuantity) {
        this.totalQuantity = totalQuantity;
    }
    public int getUnitquantity() {
        return unitQuantity;
    }

    public void setUnitquantity(int unitQuantity) {
        this.unitQuantity = unitQuantity;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}