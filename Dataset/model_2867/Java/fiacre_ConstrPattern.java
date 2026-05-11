





import java.util.List;
import java.util.ArrayList;

public class fiacre_ConstrPattern extends Pattern {

    private String name;





    private fiacre_Pattern fiacre_pattern;


    public fiacre_ConstrPattern(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public fiacre_Pattern getFiacre_pattern() {
        return fiacre_pattern;
    }

    public void setFiacre_pattern(fiacre_Pattern fiacre_pattern) {
        this.fiacre_pattern = fiacre_pattern;
    }

}