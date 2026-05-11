





import java.util.List;
import java.util.ArrayList;

public class fml_TextInput extends InputElement {

    private String Label;
    private String Content;
    private String Type;



    public fml_TextInput(
        String Label,        String Content,        String Type    ) {
        super(
        );
        this.Label = Label;
        this.Content = Content;
        this.Type = Type;
    }


    public String getLabel() {
        return Label;
    }

    public void setLabel(String Label) {
        this.Label = Label;
    }
    public String getContent() {
        return Content;
    }

    public void setContent(String Content) {
        this.Content = Content;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }


}