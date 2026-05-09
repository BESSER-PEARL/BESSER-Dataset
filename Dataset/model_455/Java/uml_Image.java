





import java.util.List;
import java.util.ArrayList;

public class uml_Image extends Element {

    private String content;
    private String format;
    private String location;



    public uml_Image(
        String content,        String format,        String location    ) {
        super(
        );
        this.content = content;
        this.format = format;
        this.location = location;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
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


}