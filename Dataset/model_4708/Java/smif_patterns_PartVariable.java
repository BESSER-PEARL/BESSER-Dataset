





import java.util.List;
import java.util.ArrayList;

public class smif_patterns_PartVariable extends TypePatternVariable {

    private String isBoundaryPart;



    public smif_patterns_PartVariable(
        String isBoundaryPart    ) {
        super(
        );
        this.isBoundaryPart = isBoundaryPart;
    }


    public String getIsboundarypart() {
        return isBoundaryPart;
    }

    public void setIsboundarypart(String isBoundaryPart) {
        this.isBoundaryPart = isBoundaryPart;
    }


}