





import java.util.List;
import java.util.ArrayList;

public class table_description_ForegroundStyleDescription  {

    private int labelSize;
    private String labelFormat;



    public table_description_ForegroundStyleDescription(
        int labelSize,        String labelFormat    ) {
        this.labelSize = labelSize;
        this.labelFormat = labelFormat;
    }


    public int getLabelsize() {
        return labelSize;
    }

    public void setLabelsize(int labelSize) {
        this.labelSize = labelSize;
    }
    public String getLabelformat() {
        return labelFormat;
    }

    public void setLabelformat(String labelFormat) {
        this.labelFormat = labelFormat;
    }


}