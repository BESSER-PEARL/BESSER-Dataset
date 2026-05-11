





import java.util.List;
import java.util.ArrayList;

public class ardlers_Program  {






    private List<ardlers_EObject> ardlers_eobjects;




    private List<ardlers_BoardDefinition> ardlers_boarddefinitions;




    private ardlers_Library ardlers_library;




    private List<ardlers_SensorImport> ardlers_sensorimports;


    public ardlers_Program(
    ) {
        this.ardlers_eobjects = new ArrayList<>();
        this.ardlers_boarddefinitions = new ArrayList<>();
        this.ardlers_sensorimports = new ArrayList<>();
    }

    public ardlers_Program(
        ArrayList<ardlers_EObject> ardlers_eobjects,        ArrayList<ardlers_BoardDefinition> ardlers_boarddefinitions,        ArrayList<ardlers_SensorImport> ardlers_sensorimports    ) {
        this.ardlers_eobjects = ardlers_eobjects;
        this.ardlers_boarddefinitions = ardlers_boarddefinitions;
        this.ardlers_sensorimports = ardlers_sensorimports;
    }


    public List<ardlers_EObject> getArdlers_eobjects() {
        return ardlers_eobjects;
    }

    public void addArdlers_eobject(Ardlers_eobject ardlers_eobject) {
        this.ardlers_eobjects.add(ardlers_eobject);
    }
    public List<ardlers_BoardDefinition> getArdlers_boarddefinitions() {
        return ardlers_boarddefinitions;
    }

    public void addArdlers_boarddefinition(Ardlers_boarddefinition ardlers_boarddefinition) {
        this.ardlers_boarddefinitions.add(ardlers_boarddefinition);
    }
    public ardlers_Library getArdlers_library() {
        return ardlers_library;
    }

    public void setArdlers_library(ardlers_Library ardlers_library) {
        this.ardlers_library = ardlers_library;
    }
    public List<ardlers_SensorImport> getArdlers_sensorimports() {
        return ardlers_sensorimports;
    }

    public void addArdlers_sensorimport(Ardlers_sensorimport ardlers_sensorimport) {
        this.ardlers_sensorimports.add(ardlers_sensorimport);
    }

}