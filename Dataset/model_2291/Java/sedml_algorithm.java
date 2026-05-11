





import java.util.List;
import java.util.ArrayList;

public class sedml_algorithm  {

    private String kisaoID;





    private sedml_uniformTimeCourse sedml_uniformtimecourse;


    public sedml_algorithm(
        String kisaoID    ) {
        this.kisaoID = kisaoID;
    }


    public String getKisaoid() {
        return kisaoID;
    }

    public void setKisaoid(String kisaoID) {
        this.kisaoID = kisaoID;
    }

    public sedml_uniformTimeCourse getSedml_uniformtimecourse() {
        return sedml_uniformtimecourse;
    }

    public void setSedml_uniformtimecourse(sedml_uniformTimeCourse sedml_uniformtimecourse) {
        this.sedml_uniformtimecourse = sedml_uniformtimecourse;
    }

}