





import java.util.List;
import java.util.ArrayList;

public class Menu  {

    private String specialCourse;
    private String desert;
    private String mainCourse;
    private String starter;





    private Order order;


    public Menu(
        String specialCourse,        String desert,        String mainCourse,        String starter    ) {
        this.specialCourse = specialCourse;
        this.desert = desert;
        this.mainCourse = mainCourse;
        this.starter = starter;
    }


    public String getSpecialcourse() {
        return specialCourse;
    }

    public void setSpecialcourse(String specialCourse) {
        this.specialCourse = specialCourse;
    }
    public String getDesert() {
        return desert;
    }

    public void setDesert(String desert) {
        this.desert = desert;
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

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}