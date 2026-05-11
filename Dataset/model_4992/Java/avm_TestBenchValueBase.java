





import java.util.List;
import java.util.ArrayList;

public class avm_TestBenchValueBase  {

    private String YPosition;
    private String Name;
    private String ID;
    private String XPosition;
    private String Notes;





    private avm_Value avm_value;


    public avm_TestBenchValueBase(
        String YPosition,        String Name,        String ID,        String XPosition,        String Notes    ) {
        this.YPosition = YPosition;
        this.Name = Name;
        this.ID = ID;
        this.XPosition = XPosition;
        this.Notes = Notes;
    }


    public String getYposition() {
        return YPosition;
    }

    public void setYposition(String YPosition) {
        this.YPosition = YPosition;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
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
    public String getNotes() {
        return Notes;
    }

    public void setNotes(String Notes) {
        this.Notes = Notes;
    }

    public avm_Value getAvm_value() {
        return avm_value;
    }

    public void setAvm_value(avm_Value avm_value) {
        this.avm_value = avm_value;
    }

}