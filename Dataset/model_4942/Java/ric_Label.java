





import java.util.List;
import java.util.ArrayList;

public class ric_Label extends ClassifiableComponent, IdentifiableComponent {

    private String format;
    private String text;





    private ric_FormControl ric_formcontrol;




    private List<ric_Event> ric_events;


    public ric_Label(
        String format,        String text    ) {
        super(
        );
        this.format = format;
        this.text = text;
        this.ric_events = new ArrayList<>();
    }

    public ric_Label(
        String format,        String text        ArrayList<ric_Event> ric_events    ) {
        this.format = format;
        this.text = text;
        this.ric_events = ric_events;
    }

    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
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