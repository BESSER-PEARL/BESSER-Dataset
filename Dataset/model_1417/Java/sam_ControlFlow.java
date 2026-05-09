





import java.util.List;
import java.util.ArrayList;

public class sam_ControlFlow extends Flow {






    private sam_ControlPort sam_controlport;




    private List<sam_ControlPort> sam_controlports;


    public sam_ControlFlow(
    ) {
        super(
        );
        this.sam_controlports = new ArrayList<>();
    }

    public sam_ControlFlow(
        ArrayList<sam_ControlPort> sam_controlports    ) {
        this.sam_controlports = sam_controlports;
    }


    public sam_ControlPort getSam_controlport() {
        return sam_controlport;
    }

    public void setSam_controlport(sam_ControlPort sam_controlport) {
        this.sam_controlport = sam_controlport;
    }
    public List<sam_ControlPort> getSam_controlports() {
        return sam_controlports;
    }

    public void addSam_controlport(Sam_controlport sam_controlport) {
        this.sam_controlports.add(sam_controlport);
    }

}