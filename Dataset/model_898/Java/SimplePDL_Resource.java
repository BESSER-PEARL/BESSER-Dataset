





import java.util.List;
import java.util.ArrayList;

public class SimplePDL_Resource extends ProcessElement {

    private int occurrences;



    public SimplePDL_Resource(
        int occurrences    ) {
        super(
        );
        this.occurrences = occurrences;
    }


    public int getOccurrences() {
        return occurrences;
    }

    public void setOccurrences(int occurrences) {
        this.occurrences = occurrences;
    }


}