





import java.util.List;
import java.util.ArrayList;

public class fiacre_FieldPattern extends Pattern {

    private String field;





    private fiacre_Pattern fiacre_pattern;


    public fiacre_FieldPattern(
        String field    ) {
        super(
        );
        this.field = field;
    }


    public String getField() {
        return field;
    }

    public void setField(String field) {
        this.field = field;
    }

    public fiacre_Pattern getFiacre_pattern() {
        return fiacre_pattern;
    }

    public void setFiacre_pattern(fiacre_Pattern fiacre_pattern) {
        this.fiacre_pattern = fiacre_pattern;
    }

}