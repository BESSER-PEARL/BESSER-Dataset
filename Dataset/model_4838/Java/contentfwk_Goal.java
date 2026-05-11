





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Goal extends Element {






    private List<contentfwk_Driver> contentfwk_drivers;




    private List<contentfwk_Objective> contentfwk_objectives;




    private contentfwk_Objective contentfwk_objective;




    private contentfwk_Goal contentfwk_goal;




    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;




    private contentfwk_Driver contentfwk_driver;


    public contentfwk_Goal(
    ) {
        super(
        );
        this.contentfwk_drivers = new ArrayList<>();
        this.contentfwk_objectives = new ArrayList<>();
    }

    public contentfwk_Goal(
        ArrayList<contentfwk_Driver> contentfwk_drivers,        ArrayList<contentfwk_Objective> contentfwk_objectives    ) {
        this.contentfwk_drivers = contentfwk_drivers;
        this.contentfwk_objectives = contentfwk_objectives;
    }


    public List<contentfwk_Driver> getContentfwk_drivers() {
        return contentfwk_drivers;
    }

    public void addContentfwk_driver(Contentfwk_driver contentfwk_driver) {
        this.contentfwk_drivers.add(contentfwk_driver);
    }
    public List<contentfwk_Objective> getContentfwk_objectives() {
        return contentfwk_objectives;
    }

    public void addContentfwk_objective(Contentfwk_objective contentfwk_objective) {
        this.contentfwk_objectives.add(contentfwk_objective);
    }
    public contentfwk_Objective getContentfwk_objective() {
        return contentfwk_objective;
    }

    public void setContentfwk_objective(contentfwk_Objective contentfwk_objective) {
        this.contentfwk_objective = contentfwk_objective;
    }
    public contentfwk_Goal getContentfwk_goal() {
        return contentfwk_goal;
    }

    public void setContentfwk_goal(contentfwk_Goal contentfwk_goal) {
        this.contentfwk_goal = contentfwk_goal;
    }
    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }
    public contentfwk_Driver getContentfwk_driver() {
        return contentfwk_driver;
    }

    public void setContentfwk_driver(contentfwk_Driver contentfwk_driver) {
        this.contentfwk_driver = contentfwk_driver;
    }

}