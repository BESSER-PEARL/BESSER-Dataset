





import java.util.List;
import java.util.ArrayList;

public class fml_SelectField extends InputElement {

    private String Type;
    private String Label;



    public fml_SelectField(
        String Type,        String Label    ) {
        super(
        );
        this.Type = Type;
        this.Label = Label;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public String getLabel() {
        return Label;
    }

    public void setLabel(String Label) {
        this.Label = Label;
    }


}