





import java.util.List;
import java.util.ArrayList;

public class ric_Image extends ObjectComponent, IdentifiableComponent, EventComponent, ClassifiableComponent {

    private String alt;
    private String src;



    public ric_Image(
        String alt,        String src    ) {
        super(
        );
        this.alt = alt;
        this.src = src;
    }


    public String getAlt() {
        return alt;
    }

    public void setAlt(String alt) {
        this.alt = alt;
    }
    public String getSrc() {
        return src;
    }

    public void setSrc(String src) {
        this.src = src;
    }


}