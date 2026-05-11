





import java.util.List;
import java.util.ArrayList;

public class avm_DomainModelParameter  {

    private String Notes;
    private String XPosition;
    private String YPosition;



    public avm_DomainModelParameter(
        String Notes,        String XPosition,        String YPosition    ) {
        this.Notes = Notes;
        this.XPosition = XPosition;
        this.YPosition = YPosition;
    }


    public String getNotes() {
        return Notes;
    }

    public void setNotes(String Notes) {
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


}