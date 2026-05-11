





import java.util.List;
import java.util.ArrayList;

public class iec61131_interfaces_Subrange extends Case_List_Element {

    private String delimiter;



    public iec61131_interfaces_Subrange(
        String delimiter    ) {
        super(
        );
        this.delimiter = delimiter;
    }


    public String getDelimiter() {
        return delimiter;
    }

    public void setDelimiter(String delimiter) {
        this.delimiter = delimiter;
    }


}