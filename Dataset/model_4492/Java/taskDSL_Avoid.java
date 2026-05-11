





import java.util.List;
import java.util.ArrayList;

public class taskDSL_Avoid  {

    private String object;
    private String color;





    private taskDSL_Detector taskdsl_detector;


    public taskDSL_Avoid(
        String object,        String color    ) {
        this.object = object;
        this.color = color;
    }


    public String getObject() {
        return object;
    }

    public void setObject(String object) {
        this.object = object;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public taskDSL_Detector getTaskdsl_detector() {
        return taskdsl_detector;
    }

    public void setTaskdsl_detector(taskDSL_Detector taskdsl_detector) {
        this.taskdsl_detector = taskdsl_detector;
    }

}