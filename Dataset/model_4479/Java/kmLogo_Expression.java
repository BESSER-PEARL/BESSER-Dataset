





import java.util.List;
import java.util.ArrayList;

public class kmLogo_Expression extends Instruction {






    private kmLogo_ControlStructure kmlogo_controlstructure;




    private kmLogo_ProcCall kmlogo_proccall;


    public kmLogo_Expression(
    ) {
        super(
        );
    }



    public kmLogo_ControlStructure getKmlogo_controlstructure() {
        return kmlogo_controlstructure;
    }

    public void setKmlogo_controlstructure(kmLogo_ControlStructure kmlogo_controlstructure) {
        this.kmlogo_controlstructure = kmlogo_controlstructure;
    }
    public kmLogo_ProcCall getKmlogo_proccall() {
        return kmlogo_proccall;
    }

    public void setKmlogo_proccall(kmLogo_ProcCall kmlogo_proccall) {
        this.kmlogo_proccall = kmlogo_proccall;
    }

}