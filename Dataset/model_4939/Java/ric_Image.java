





import java.util.List;
import java.util.ArrayList;

public class ric_Image extends IdentifiableComponent, ObjectComponent, ClassifiableComponent, EventComponent {

    private String src;
    private String alt;



    public ric_Image(
        String src,        String alt    ) {
        super(
        );
        this.src = src;
        this.alt = alt;
    }


    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }
    public String getAlt() {
        return alt;
    }

    public void setAlt(String alt) {
        this.alt = alt;
    }


}