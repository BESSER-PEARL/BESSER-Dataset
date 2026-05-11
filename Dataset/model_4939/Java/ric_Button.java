





import java.util.List;
import java.util.ArrayList;

public class ric_Button extends FormControl {

    private String type;
    private boolean disabled;
    private String image;



    public ric_Button(
        String type,        boolean disabled,        String image    ) {
        super(
        );
        this.type = type;
        this.disabled = disabled;
        this.image = image;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getDisabled() {
        return disabled;
    }

    public void setDisabled(boolean disabled) {
        this.disabled = disabled;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }


}