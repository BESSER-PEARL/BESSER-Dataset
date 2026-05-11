





import java.util.List;
import java.util.ArrayList;

public class sedml_task  {

    private String name;
    private String id;





    private sedml_listOfTasks sedml_listoftasks;




    private sedml_uniformTimeCourse sedml_uniformtimecourse;




    private sedml_model sedml_model;


    public sedml_task(
        String name,        String id    ) {
        this.name = name;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public sedml_listOfTasks getSedml_listoftasks() {
        return sedml_listoftasks;
    }

    public void setSedml_listoftasks(sedml_listOfTasks sedml_listoftasks) {
        this.sedml_listoftasks = sedml_listoftasks;
    }
    public sedml_uniformTimeCourse getSedml_uniformtimecourse() {
        return sedml_uniformtimecourse;
    }

    public void setSedml_uniformtimecourse(sedml_uniformTimeCourse sedml_uniformtimecourse) {
        this.sedml_uniformtimecourse = sedml_uniformtimecourse;
    }
    public sedml_model getSedml_model() {
        return sedml_model;
    }

    public void setSedml_model(sedml_model sedml_model) {
        this.sedml_model = sedml_model;
    }

}