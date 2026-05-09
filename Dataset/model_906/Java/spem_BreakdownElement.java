





import java.util.List;
import java.util.ArrayList;

public class spem_BreakdownElement extends ProcessElement {

    private boolean isOptional;
    private boolean hasMultipleOccurrences;
    private boolean isPlanned;



    public spem_BreakdownElement(
        boolean isOptional,        boolean hasMultipleOccurrences,        boolean isPlanned    ) {
        super(
        );
        this.isOptional = isOptional;
        this.hasMultipleOccurrences = hasMultipleOccurrences;
        this.isPlanned = isPlanned;
    }


    public boolean getIsoptional() {
        return isOptional;
    }

    public void setIsoptional(boolean isOptional) {
        this.isOptional = isOptional;
    }
    public boolean getHasmultipleoccurrences() {
        return hasMultipleOccurrences;
    }

    public void setHasmultipleoccurrences(boolean hasMultipleOccurrences) {
        this.hasMultipleOccurrences = hasMultipleOccurrences;
    }
    public boolean getIsplanned() {
        return isPlanned;
    }

    public void setIsplanned(boolean isPlanned) {
        this.isPlanned = isPlanned;
    }


}