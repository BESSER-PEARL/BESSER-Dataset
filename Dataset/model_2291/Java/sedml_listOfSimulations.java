





import java.util.List;
import java.util.ArrayList;

public class sedml_listOfSimulations  {






    private List<sedml_uniformTimeCourse> sedml_uniformtimecourses;




    private sedml_sedML sedml_sedml;


    public sedml_listOfSimulations(
    ) {
        this.sedml_uniformtimecourses = new ArrayList<>();
    }

    public sedml_listOfSimulations(
        ArrayList<sedml_uniformTimeCourse> sedml_uniformtimecourses    ) {
        this.sedml_uniformtimecourses = sedml_uniformtimecourses;
    }


    public List<sedml_uniformTimeCourse> getSedml_uniformtimecourses() {
        return sedml_uniformtimecourses;
    }

    public void addSedml_uniformtimecourse(Sedml_uniformtimecourse sedml_uniformtimecourse) {
        this.sedml_uniformtimecourses.add(sedml_uniformtimecourse);
    }
    public sedml_sedML getSedml_sedml() {
        return sedml_sedml;
    }

    public void setSedml_sedml(sedml_sedML sedml_sedml) {
        this.sedml_sedml = sedml_sedml;
    }

}