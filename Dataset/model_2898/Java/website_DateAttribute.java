





import java.util.List;
import java.util.ArrayList;

public class website_DateAttribute extends EntityAttribute {

    private String details;
    private String format;



    public website_DateAttribute(
        String details,        String format    ) {
        super(
        );
        this.details = details;
        this.format = format;
    }


    public String getDetails() {
        return details;
    }

    public void setDetails(String details) {
        this.details = details;
    }
    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }


}