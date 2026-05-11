





import java.util.List;
import java.util.ArrayList;

public class draw2d_RoundedRectangle extends Shape {

    private String cornerDimensions;



    public draw2d_RoundedRectangle(
        String cornerDimensions    ) {
        super(
        );
        this.cornerDimensions = cornerDimensions;
    }


    public String getCornerdimensions() {
        return cornerDimensions;
    }

    public void setCornerdimensions(String cornerDimensions) {
        this.cornerDimensions = cornerDimensions;
    }


}