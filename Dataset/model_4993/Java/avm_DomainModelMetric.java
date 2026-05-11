





import java.util.List;
import java.util.ArrayList;

public class avm_DomainModelMetric  {

    private String XPosition;
    private String YPosition;
    private String ID;
    private String Notes;



    public avm_DomainModelMetric(
        String XPosition,        String YPosition,        String ID,        String Notes    ) {
        this.XPosition = XPosition;
        this.YPosition = YPosition;
        this.ID = ID;
        this.Notes = Notes;
    }


    public String getXposition() {
        return XPosition;
    }

    public void setXposition(String XPosition) {
        this.XPosition = XPosition;
    }
    public String getYposition() {
        return YPosition;
    }

    public void setYposition(String YPosition) {
        this.YPosition = YPosition;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getNotes() {
        return Notes;
    }

    public void setNotes(String Notes) {
        this.Notes = Notes;
    }


}