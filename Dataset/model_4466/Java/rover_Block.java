





import java.util.List;
import java.util.ArrayList;

public class rover_Block  {

    private String name;





    private List<rover_Tansition> rover_tansitions;




    private rover_Program rover_program;


    public rover_Block(
        String name    ) {
        this.name = name;
        this.rover_tansitions = new ArrayList<>();
    }

    public rover_Block(
        String name        ArrayList<rover_Tansition> rover_tansitions    ) {
        this.name = name;
        this.rover_tansitions = rover_tansitions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<rover_Tansition> getRover_tansitions() {
        return rover_tansitions;
    }

    public void addRover_tansition(Rover_tansition rover_tansition) {
        this.rover_tansitions.add(rover_tansition);
    }
    public rover_Program getRover_program() {
        return rover_program;
    }

    public void setRover_program(rover_Program rover_program) {
        this.rover_program = rover_program;
    }

}