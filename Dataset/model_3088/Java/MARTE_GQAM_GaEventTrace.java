





import java.util.List;
import java.util.ArrayList;

public class MARTE_GQAM_GaEventTrace  {

    private String content;
    private String location;
    private String format;



    public MARTE_GQAM_GaEventTrace(
        String content,        String location,        String format    ) {
        this.content = content;
        this.location = location;
        this.format = format;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }


}