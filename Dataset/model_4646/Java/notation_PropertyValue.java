





import java.util.List;
import java.util.ArrayList;

public class notation_PropertyValue extends StringObjectConverter {

    private String rawValue;



    public notation_PropertyValue(
        String rawValue    ) {
        super(
        );
        this.rawValue = rawValue;
    }


    public String getRawvalue() {
        return rawValue;
    }

    public void setRawvalue(String rawValue) {
        this.rawValue = rawValue;
    }


}