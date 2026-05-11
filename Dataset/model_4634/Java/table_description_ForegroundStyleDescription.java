





import java.util.List;
import java.util.ArrayList;

public class table_description_ForegroundStyleDescription  {

    private String labelFormat;
    private int labelSize;



    public table_description_ForegroundStyleDescription(
        String labelFormat,        int labelSize    ) {
        this.labelFormat = labelFormat;
        this.labelSize = labelSize;
    }


    public String getLabelformat() {
        return labelFormat;
    }

    public void setLabelformat(String labelFormat) {
        this.labelFormat = labelFormat;
    }
    public int getLabelsize() {
        return labelSize;
    }

    public void setLabelsize(int labelSize) {
        this.labelSize = labelSize;
    }


}