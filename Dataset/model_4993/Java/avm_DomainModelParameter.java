





import java.util.List;
import java.util.ArrayList;

public class avm_DomainModelParameter  {

    private String XPosition;
    private String Notes;
    private String YPosition;



    public avm_DomainModelParameter(
        String XPosition,        String Notes,        String YPosition    ) {
        this.XPosition = XPosition;
        this.Notes = Notes;
        this.YPosition = YPosition;
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
    public String getYposition() {
        return YPosition;
    }

    public void setYposition(String YPosition) {
        this.YPosition = YPosition;
    }


}