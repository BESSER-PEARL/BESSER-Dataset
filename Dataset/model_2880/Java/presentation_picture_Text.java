





import java.util.List;
import java.util.ArrayList;

public class presentation_picture_Text extends Graphic2D {






    private List<TextParameter> textparameters;


    public presentation_picture_Text(
    ) {
        super(
        );
        this.textparameters = new ArrayList<>();
    }

    public presentation_picture_Text(
        ArrayList<TextParameter> textparameters    ) {
        this.textparameters = textparameters;
    }


    public List<TextParameter> getTextparameters() {
        return textparameters;
    }

    public void addTextparameter(Textparameter textparameter) {
        this.textparameters.add(textparameter);
    }

}