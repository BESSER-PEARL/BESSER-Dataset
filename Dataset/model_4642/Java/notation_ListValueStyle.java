





import java.util.List;
import java.util.ArrayList;

public class notation_ListValueStyle extends DataTypeStyle {

    private String rawValuesList;



    public notation_ListValueStyle(
        String rawValuesList    ) {
        super(
        );
        this.rawValuesList = rawValuesList;
    }


    public String getRawvalueslist() {
        return rawValuesList;
    }

    public void setRawvalueslist(String rawValuesList) {
        this.rawValuesList = rawValuesList;
    }


}