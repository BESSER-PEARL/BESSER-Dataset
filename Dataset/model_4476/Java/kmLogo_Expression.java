





import java.util.List;
import java.util.ArrayList;

public class kmLogo_Expression extends Instruction {






    private kmLogo_ProcCall kmlogo_proccall;




    private kmLogo_BinaryExp kmlogo_binaryexp;




    private kmLogo_ControlStructure kmlogo_controlstructure;




    private kmLogo_BinaryExp kmlogo_binaryexp;


    public kmLogo_Expression(
    ) {
        super(
        );
    }



    public kmLogo_ProcCall getKmlogo_proccall() {
        return kmlogo_proccall;
    }

    public void setKmlogo_proccall(kmLogo_ProcCall kmlogo_proccall) {
        this.kmlogo_proccall = kmlogo_proccall;
    }
    public kmLogo_BinaryExp getKmlogo_binaryexp() {
        return kmlogo_binaryexp;
    }

    public void setKmlogo_binaryexp(kmLogo_BinaryExp kmlogo_binaryexp) {
        this.kmlogo_binaryexp = kmlogo_binaryexp;
    }
    public kmLogo_ControlStructure getKmlogo_controlstructure() {
        return kmlogo_controlstructure;
    }

    public void setKmlogo_controlstructure(kmLogo_ControlStructure kmlogo_controlstructure) {
        this.kmlogo_controlstructure = kmlogo_controlstructure;
    }
    public kmLogo_BinaryExp getKmlogo_binaryexp() {
        return kmlogo_binaryexp;
    }

    public void setKmlogo_binaryexp(kmLogo_BinaryExp kmlogo_binaryexp) {
        this.kmlogo_binaryexp = kmlogo_binaryexp;
    }

}