





import java.util.List;
import java.util.ArrayList;

public class conf101_Person extends NamedElement {






    private conf101_SteeringComitee conf101_steeringcomitee;




    private conf101_ProgramComitee conf101_programcomitee;


    public conf101_Person(
    ) {
        super(
        );
    }



    public conf101_SteeringComitee getConf101_steeringcomitee() {
        return conf101_steeringcomitee;
    }

    public void setConf101_steeringcomitee(conf101_SteeringComitee conf101_steeringcomitee) {
        this.conf101_steeringcomitee = conf101_steeringcomitee;
    }
    public conf101_ProgramComitee getConf101_programcomitee() {
        return conf101_programcomitee;
    }

    public void setConf101_programcomitee(conf101_ProgramComitee conf101_programcomitee) {
        this.conf101_programcomitee = conf101_programcomitee;
    }

}