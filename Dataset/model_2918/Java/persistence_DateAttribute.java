





import java.util.List;
import java.util.ArrayList;

public class persistence_DateAttribute extends EntityAttribute {

    private String format;
    private String details;



    public persistence_DateAttribute(
        String format,        String details    ) {
        super(
        );
        this.format = format;
        this.details = details;
    }


    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }
    public String getDetails() {
        return details;
    }

    public void setDetails(String details) {
        this.details = details;
    }


}