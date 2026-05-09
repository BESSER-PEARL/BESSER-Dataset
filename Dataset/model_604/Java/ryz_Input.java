





import java.util.List;
import java.util.ArrayList;

public class ryz_Input extends PresentationFormElement {

    private boolean isHidden;
    private String inputDataType;
    private boolean isReadOnly;



    public ryz_Input(
        boolean isHidden,        String inputDataType,        boolean isReadOnly    ) {
        super(
        );
        this.isHidden = isHidden;
        this.inputDataType = inputDataType;
        this.isReadOnly = isReadOnly;
    }


    public boolean getIshidden() {
        return isHidden;
    }

    public void setIshidden(boolean isHidden) {
        this.isHidden = isHidden;
    }
    public String getInputdatatype() {
        return inputDataType;
    }

    public void setInputdatatype(String inputDataType) {
        this.inputDataType = inputDataType;
    }
    public boolean getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(boolean isReadOnly) {
        this.isReadOnly = isReadOnly;
    }


}