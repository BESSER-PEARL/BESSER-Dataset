





import java.util.List;
import java.util.ArrayList;

public class Maude_Operation extends ModElement {

    private String name;
    private String atts;



    public Maude_Operation(
        String name,        String atts    ) {
        super(
        );
        this.name = name;
        this.atts = atts;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAtts() {
        return atts;
    }

    public void setAtts(String atts) {
        this.atts = atts;
    }


}