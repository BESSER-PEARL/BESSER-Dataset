





import java.util.List;
import java.util.ArrayList;

public class cellsheet_NumericCell extends Cell {

    private String value;



    public cellsheet_NumericCell(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}