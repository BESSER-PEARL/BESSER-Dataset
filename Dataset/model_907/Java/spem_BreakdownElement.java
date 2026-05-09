





import java.util.List;
import java.util.ArrayList;

public class spem_BreakdownElement extends ProcessElement {

    private boolean hasMultipleOccurrences;
    private boolean isOptional;
    private boolean isPlanned;



    public spem_BreakdownElement(
        boolean hasMultipleOccurrences,        boolean isOptional,        boolean isPlanned    ) {
        super(
        );
        this.hasMultipleOccurrences = hasMultipleOccurrences;
        this.isOptional = isOptional;
        this.isPlanned = isPlanned;
    }


    public boolean getHasmultipleoccurrences() {
        return hasMultipleOccurrences;
    }

    public void setHasmultipleoccurrences(boolean hasMultipleOccurrences) {
        this.hasMultipleOccurrences = hasMultipleOccurrences;
    }
    public boolean getIsoptional() {
        return isOptional;
    }

    public void setIsoptional(boolean isOptional) {
        this.isOptional = isOptional;
    }
    public boolean getIsplanned() {
        return isPlanned;
    }

    public void setIsplanned(boolean isPlanned) {
        this.isPlanned = isPlanned;
    }


}