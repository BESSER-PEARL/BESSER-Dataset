





import java.util.List;
import java.util.ArrayList;

public class ryz_Button extends PresentationFormElement {

    private String buttonType;



    public ryz_Button(
        String buttonType    ) {
        super(
        );
        this.buttonType = buttonType;
    }


    public String getButtontype() {
        return buttonType;
    }

    public void setButtontype(String buttonType) {
        this.buttonType = buttonType;
    }


}