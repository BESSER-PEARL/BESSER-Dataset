





import java.util.List;
import java.util.ArrayList;

public class roverml_RoverSystem  {






    private List<roverml_Rover> roverml_rovers;




    private List<roverml_RoverProgram> roverml_roverprograms;


    public roverml_RoverSystem(
    ) {
        this.roverml_rovers = new ArrayList<>();
        this.roverml_roverprograms = new ArrayList<>();
    }

    public roverml_RoverSystem(
        ArrayList<roverml_Rover> roverml_rovers,        ArrayList<roverml_RoverProgram> roverml_roverprograms    ) {
        this.roverml_rovers = roverml_rovers;
        this.roverml_roverprograms = roverml_roverprograms;
    }


    public List<roverml_Rover> getRoverml_rovers() {
        return roverml_rovers;
    }

    public void addRoverml_rover(Roverml_rover roverml_rover) {
        this.roverml_rovers.add(roverml_rover);
    }
    public List<roverml_RoverProgram> getRoverml_roverprograms() {
        return roverml_roverprograms;
    }

    public void addRoverml_roverprogram(Roverml_roverprogram roverml_roverprogram) {
        this.roverml_roverprograms.add(roverml_roverprogram);
    }

}