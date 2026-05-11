





import java.util.List;
import java.util.ArrayList;

public class sedml_uniformTimeCourse  {

    private int numberOfPoints;
    private String id;
    private int initialTime;
    private int outputEndTime;
    private int outputStartTime;



    public sedml_uniformTimeCourse(
        int numberOfPoints,        String id,        int initialTime,        int outputEndTime,        int outputStartTime    ) {
        this.numberOfPoints = numberOfPoints;
        this.id = id;
        this.initialTime = initialTime;
        this.outputEndTime = outputEndTime;
        this.outputStartTime = outputStartTime;
    }


    public int getNumberofpoints() {
        return numberOfPoints;
    }

    public void setNumberofpoints(int numberOfPoints) {
        this.numberOfPoints = numberOfPoints;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getInitialtime() {
        return initialTime;
    }

    public void setInitialtime(int initialTime) {
        this.initialTime = initialTime;
    }
    public int getOutputendtime() {
        return outputEndTime;
    }

    public void setOutputendtime(int outputEndTime) {
        this.outputEndTime = outputEndTime;
    }
    public int getOutputstarttime() {
        return outputStartTime;
    }

    public void setOutputstarttime(int outputStartTime) {
        this.outputStartTime = outputStartTime;
    }


}