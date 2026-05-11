





import java.util.List;
import java.util.ArrayList;

public class trace_NumberValueChangeEvent extends ValueChangeEvent {

    private String value;



    public trace_NumberValueChangeEvent(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}