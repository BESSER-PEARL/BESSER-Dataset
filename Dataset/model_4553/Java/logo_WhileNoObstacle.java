





import java.util.List;
import java.util.ArrayList;

public class logo_WhileNoObstacle extends Command {

    private float distance;





    private List<logo_Command> logo_commands;


    public logo_WhileNoObstacle(
        float distance    ) {
        super(
        );
        this.distance = distance;
        this.logo_commands = new ArrayList<>();
    }

    public logo_WhileNoObstacle(
        float distance        ArrayList<logo_Command> logo_commands    ) {
        this.distance = distance;
        this.logo_commands = logo_commands;
    }

    public float getDistance() {
        return distance;
    }

    public void setDistance(float distance) {
        this.distance = distance;
    }

    public List<logo_Command> getLogo_commands() {
        return logo_commands;
    }

    public void addLogo_command(Logo_command logo_command) {
        this.logo_commands.add(logo_command);
    }

}