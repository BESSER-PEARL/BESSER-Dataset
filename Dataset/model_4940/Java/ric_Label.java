





import java.util.List;
import java.util.ArrayList;

public class ric_Label extends ClassifiableComponent, IdentifiableComponent {

    private String text;
    private String format;



    public ric_Label(
        String text,        String format    ) {
        super(
        );
        this.text = text;
        this.format = format;
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


}