





import java.util.List;
import java.util.ArrayList;

public class Maude_Operation extends ModElement {

    private String atts;
    private String name;



    public Maude_Operation(
        String atts,        String name    ) {
        super(
        );
        this.atts = atts;
        this.name = name;
    }


    public String getAtts() {
        return atts;
    }

    public void setAtts(String atts) {
        this.atts = atts;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}