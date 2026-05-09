





import java.util.List;
import java.util.ArrayList;

public class sam_ModelContent extends NamedItem {






    private sam_MultiPort sam_multiport;




    private sam_System sam_system;




    private sam_System sam_system;




    private List<sam_MultiPort> sam_multiports;


    public sam_ModelContent(
    ) {
        super(
        );
        this.sam_multiports = new ArrayList<>();
    }

    public sam_ModelContent(
        ArrayList<sam_MultiPort> sam_multiports    ) {
        this.sam_multiports = sam_multiports;
    }


    public sam_MultiPort getSam_multiport() {
        return sam_multiport;
    }

    public void setSam_multiport(sam_MultiPort sam_multiport) {
        this.sam_multiport = sam_multiport;
    }
    public sam_System getSam_system() {
        return sam_system;
    }

    public void setSam_system(sam_System sam_system) {
        this.sam_system = sam_system;
    }
    public sam_System getSam_system() {
        return sam_system;
    }

    public void setSam_system(sam_System sam_system) {
        this.sam_system = sam_system;
    }
    public List<sam_MultiPort> getSam_multiports() {
        return sam_multiports;
    }

    public void addSam_multiport(Sam_multiport sam_multiport) {
        this.sam_multiports.add(sam_multiport);
    }

}