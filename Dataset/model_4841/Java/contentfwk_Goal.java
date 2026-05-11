





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Goal extends Element {






    private contentfwk_Driver contentfwk_driver;




    private contentfwk_Goal contentfwk_goal;




    private List<contentfwk_Driver> contentfwk_drivers;




    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;




    private List<contentfwk_Goal> contentfwk_goals;


    public contentfwk_Goal(
    ) {
        super(
        );
        this.contentfwk_drivers = new ArrayList<>();
        this.contentfwk_goals = new ArrayList<>();
    }

    public contentfwk_Goal(
        ArrayList<contentfwk_Driver> contentfwk_drivers,        ArrayList<contentfwk_Goal> contentfwk_goals    ) {
        this.contentfwk_drivers = contentfwk_drivers;
        this.contentfwk_goals = contentfwk_goals;
    }


    public contentfwk_Driver getContentfwk_driver() {
        return contentfwk_driver;
    }

    public void setContentfwk_driver(contentfwk_Driver contentfwk_driver) {
        this.contentfwk_driver = contentfwk_driver;
    }
    public contentfwk_Goal getContentfwk_goal() {
        return contentfwk_goal;
    }

    public void setContentfwk_goal(contentfwk_Goal contentfwk_goal) {
        this.contentfwk_goal = contentfwk_goal;
    }
    public List<contentfwk_Driver> getContentfwk_drivers() {
        return contentfwk_drivers;
    }

    public void addContentfwk_driver(Contentfwk_driver contentfwk_driver) {
        this.contentfwk_drivers.add(contentfwk_driver);
    }
    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }
    public List<contentfwk_Goal> getContentfwk_goals() {
        return contentfwk_goals;
    }

    public void addContentfwk_goal(Contentfwk_goal contentfwk_goal) {
        this.contentfwk_goals.add(contentfwk_goal);
    }

}