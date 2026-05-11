





import java.util.List;
import java.util.ArrayList;

public class becontent_Year extends NotStructuredElement {

    private String label;
    private boolean isMandatory;
    private int end;
    private int start;
    private String name;



    public becontent_Year(
        String label,        boolean isMandatory,        int end,        int start,        String name    ) {
        super(
        );
        this.label = label;
        this.isMandatory = isMandatory;
        this.end = end;
        this.start = start;
        this.name = name;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public boolean getIsmandatory() {
        return isMandatory;
    }

    public void setIsmandatory(boolean isMandatory) {
        this.isMandatory = isMandatory;
    }
    public int getEnd() {
        return end;
    }

    public void setEnd(int end) {
        this.end = end;
    }
    public int getStart() {
        return start;
    }

    public void setStart(int start) {
        this.start = start;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}