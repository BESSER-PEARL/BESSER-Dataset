





import java.util.List;
import java.util.ArrayList;

public class Styling_ModelPattern extends Pattern {

    private String attributeName;



    public Styling_ModelPattern(
        String attributeName    ) {
        super(
        );
        this.attributeName = attributeName;
    }


    public String getAttributename() {
        return attributeName;
    }

    public void setAttributename(String attributeName) {
        this.attributeName = attributeName;
    }


}