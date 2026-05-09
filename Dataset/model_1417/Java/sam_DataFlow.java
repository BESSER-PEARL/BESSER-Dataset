





import java.util.List;
import java.util.ArrayList;

public class sam_DataFlow extends Flow {

    private String type;





    private List<sam_DataPort> sam_dataports;




    private sam_DataPort sam_dataport;


    public sam_DataFlow(
        String type    ) {
        super(
        );
        this.type = type;
        this.sam_dataports = new ArrayList<>();
    }

    public sam_DataFlow(
        String type        ArrayList<sam_DataPort> sam_dataports    ) {
        this.type = type;
        this.sam_dataports = sam_dataports;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<sam_DataPort> getSam_dataports() {
        return sam_dataports;
    }

    public void addSam_dataport(Sam_dataport sam_dataport) {
        this.sam_dataports.add(sam_dataport);
    }
    public sam_DataPort getSam_dataport() {
        return sam_dataport;
    }

    public void setSam_dataport(sam_DataPort sam_dataport) {
        this.sam_dataport = sam_dataport;
    }

}