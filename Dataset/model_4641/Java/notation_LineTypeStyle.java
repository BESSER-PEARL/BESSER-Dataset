





import java.util.List;
import java.util.ArrayList;

public class notation_LineTypeStyle extends Style {

    private String lineType;



    public notation_LineTypeStyle(
        String lineType    ) {
        super(
        );
        this.lineType = lineType;
    }


    public String getLinetype() {
        return lineType;
    }

    public void setLinetype(String lineType) {
        this.lineType = lineType;
    }


}