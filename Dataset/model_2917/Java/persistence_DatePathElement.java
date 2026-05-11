





import java.util.List;
import java.util.ArrayList;

public class persistence_DatePathElement extends PathElement {

    private String format;



    public persistence_DatePathElement(
        String format    ) {
        super(
        );
        this.format = format;
    }


    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }


}