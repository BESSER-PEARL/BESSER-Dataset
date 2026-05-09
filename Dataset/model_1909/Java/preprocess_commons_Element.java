





import java.util.List;
import java.util.ArrayList;

public class preprocess_commons_Element  {






    private List<CobolLine> cobollines;


    public preprocess_commons_Element(
    ) {
        this.cobollines = new ArrayList<>();
    }

    public preprocess_commons_Element(
        ArrayList<CobolLine> cobollines    ) {
        this.cobollines = cobollines;
    }


    public List<CobolLine> getCobollines() {
        return cobollines;
    }

    public void addCobolline(Cobolline cobolline) {
        this.cobollines.add(cobolline);
    }

}