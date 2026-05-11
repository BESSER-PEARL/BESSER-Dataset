





import java.util.List;
import java.util.ArrayList;

public class avm_eda_PcbLayoutConstraint extends ContainerFeature {

    private String YPosition;
    private String Notes;
    private String XPosition;



    public avm_eda_PcbLayoutConstraint(
        String YPosition,        String Notes,        String XPosition    ) {
        super(
        );
        this.YPosition = YPosition;
        this.Notes = Notes;
        this.XPosition = XPosition;
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
    public String getXposition() {
        return XPosition;
    }

    public void setXposition(String XPosition) {
        this.XPosition = XPosition;
    }


}