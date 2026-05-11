





import java.util.List;
import java.util.ArrayList;

public class avm_TestBenchValueBase  {

    private String Name;
    private String YPosition;
    private String Notes;
    private String ID;
    private String XPosition;



    public avm_TestBenchValueBase(
        String Name,        String YPosition,        String Notes,        String ID,        String XPosition    ) {
        this.Name = Name;
        this.YPosition = YPosition;
        this.Notes = Notes;
        this.ID = ID;
        this.XPosition = XPosition;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getYposition() {
        return YPosition;
    }

    public void setYposition(String YPosition) {
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


}