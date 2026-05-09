





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Image extends Element {

    private String format;
    private String location;
    private String content;



    public UMLModel_Image(
        String format,        String location,        String content    ) {
        super(
        );
        this.format = format;
        this.location = location;
        this.content = content;
    }


    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }


}