





import java.util.List;
import java.util.ArrayList;

public class ric_Button extends FormControl {

    private String type;
    private String image;
    private boolean disabled;



    public ric_Button(
        String type,        String image,        boolean disabled    ) {
        super(
        );
        this.type = type;
        this.image = image;
        this.disabled = disabled;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public boolean getDisabled() {
        return disabled;
    }

    public void setDisabled(boolean disabled) {
        this.disabled = disabled;
    }


}