





import java.util.List;
import java.util.ArrayList;

public class ric_Label extends IdentifiableComponent, ClassifiableComponent {

    private String text;
    private String format;





    private ric_FormControl ric_formcontrol;




    private List<ric_Event> ric_events;


    public ric_Label(
        String text,        String format    ) {
        super(
        );
        this.text = text;
        this.format = format;
        this.ric_events = new ArrayList<>();
    }

    public ric_Label(
        String text,        String format        ArrayList<ric_Event> ric_events    ) {
        this.text = text;
        this.format = format;
        this.ric_events = ric_events;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }

    public ric_FormControl getRic_formcontrol() {
        return ric_formcontrol;
    }

    public void setRic_formcontrol(ric_FormControl ric_formcontrol) {
        this.ric_formcontrol = ric_formcontrol;
    }
    public List<ric_Event> getRic_events() {
        return ric_events;
    }

    public void addRic_event(Ric_event ric_event) {
        this.ric_events.add(ric_event);
    }

}