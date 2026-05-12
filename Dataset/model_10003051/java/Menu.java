





import java.util.List;
import java.util.ArrayList;

public class Menu  {

    private String desert;
    private String starter;
    private String mainCourse;
    private String specialCourse;





    private Order order;


    public Menu(
        String desert,        String starter,        String mainCourse,        String specialCourse    ) {
        this.desert = desert;
        this.starter = starter;
        this.mainCourse = mainCourse;
        this.specialCourse = specialCourse;
    }


    public String getDesert() {
        return desert;
    }

    public void setDesert(String desert) {
        this.desert = desert;
    }
    public String getStarter() {
        return starter;
    }

    public void setStarter(String starter) {
        this.starter = starter;
    }
    public String getMaincourse() {
        return mainCourse;
    }

    public void setMaincourse(String mainCourse) {
        this.mainCourse = mainCourse;
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