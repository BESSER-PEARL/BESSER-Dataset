





import java.util.List;
import java.util.ArrayList;

public class avm_DomainModelMetric  {

    private String Notes;
    private String ID;
    private String XPosition;
    private String YPosition;





    private avm_Value avm_value;


    public avm_DomainModelMetric(
        String Notes,        String ID,        String XPosition,        String YPosition    ) {
        this.Notes = Notes;
        this.ID = ID;
        this.XPosition = XPosition;
        this.YPosition = YPosition;
    }


    public String getNotes() {
        return Notes;
    }

    public void setNotes(String Notes) {
        this.Notes = Notes;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
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

    public avm_Value getAvm_value() {
        return avm_value;
    }

    public void setAvm_value(avm_Value avm_value) {
        this.avm_value = avm_value;
    }

}