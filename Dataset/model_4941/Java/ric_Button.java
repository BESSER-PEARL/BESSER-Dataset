





import java.util.List;
import java.util.ArrayList;

public class ric_Button extends FormControl {

    private boolean disabled;
    private String image;
    private String type;



    public ric_Button(
        boolean disabled,        String image,        String type    ) {
        super(
        );
        this.disabled = disabled;
        this.image = image;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}