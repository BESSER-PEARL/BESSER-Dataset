





import java.util.List;
import java.util.ArrayList;

public class di_Container extends View {

    private String allLines;
    private String allShapes;



    public di_Container(
        String allLines,        String allShapes    ) {
        super(
        );
        this.allLines = allLines;
        this.allShapes = allShapes;
    }


    public String getAlllines() {
        return allLines;
    }

    public void setAlllines(String allLines) {
        this.allLines = allLines;
    }
    public String getAllshapes() {
        return allShapes;
    }

    public void setAllshapes(String allShapes) {
        this.allShapes = allShapes;
    }


}