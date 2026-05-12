





import java.util.List;
import java.util.ArrayList;

public class Menu  {

    private String desert;
    private String mainCourse;
    private String starter;
    private String specialCourse;





    private Order order;


    public Menu(
        String desert,        String mainCourse,        String starter,        String specialCourse    ) {
        this.desert = desert;
        this.mainCourse = mainCourse;
        this.starter = starter;
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
    public String getSpecialcourse() {
        return specialCourse;
    }

    public void setSpecialcourse(String specialCourse) {
        this.specialCourse = specialCourse;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}