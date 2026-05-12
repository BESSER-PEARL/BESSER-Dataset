





import java.util.List;
import java.util.ArrayList;

public class Menu  {

    private String specialCourse;
    private String mainCourse;
    private String starter;
    private String desert;





    private Order order;


    public Menu(
        String specialCourse,        String mainCourse,        String starter,        String desert    ) {
        this.specialCourse = specialCourse;
        this.mainCourse = mainCourse;
        this.starter = starter;
        this.desert = desert;
    }


    public String getSpecialcourse() {
        return specialCourse;
    }

    public void setSpecialcourse(String specialCourse) {
        this.specialCourse = specialCourse;
    }
    public String getMaincourse() {
        return mainCourse;
    }

    public void setMaincourse(String mainCourse) {
        this.mainCourse = mainCourse;
    }
    public String getStarter() {
        return starter;
    }

    public void setStarter(String starter) {
        this.starter = starter;
    }
    public String getDesert() {
        return desert;
    }

    public void setDesert(String desert) {
        this.desert = desert;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}