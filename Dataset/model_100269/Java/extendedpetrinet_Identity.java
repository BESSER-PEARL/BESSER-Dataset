





import java.util.List;
import java.util.ArrayList;

public class extendedpetrinet_Identity extends Attribute {

    private int text;





    private extendedpetrinet_Arc extendedpetrinet_arc;


    public extendedpetrinet_Identity(
        int text    ) {
        super(
        );
        this.text = text;
    }


    public int getText() {
        return text;
    }

    public void setText(int text) {
        this.text = text;
    }

    public extendedpetrinet_Arc getExtendedpetrinet_arc() {
        return extendedpetrinet_arc;
    }

    public void setExtendedpetrinet_arc(extendedpetrinet_Arc extendedpetrinet_arc) {
        this.extendedpetrinet_arc = extendedpetrinet_arc;
    }

}