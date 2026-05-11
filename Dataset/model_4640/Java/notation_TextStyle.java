





import java.util.List;
import java.util.ArrayList;

public class notation_TextStyle extends Style {

    private String textAlignment;



    public notation_TextStyle(
        String textAlignment    ) {
        super(
        );
        this.textAlignment = textAlignment;
    }


    public String getTextalignment() {
        return textAlignment;
    }

    public void setTextalignment(String textAlignment) {
        this.textAlignment = textAlignment;
    }


}