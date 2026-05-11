





import java.util.List;
import java.util.ArrayList;

public class trace_DataSizeValueChangeEvent extends ValueChangeEvent {

    private String value;



    public trace_DataSizeValueChangeEvent(
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