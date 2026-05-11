





import java.util.List;
import java.util.ArrayList;

public class di_Node extends View {

    private String allIncomingLines;
    private String allOutgoingLines;



    public di_Node(
        String allIncomingLines,        String allOutgoingLines    ) {
        super(
        );
        this.allIncomingLines = allIncomingLines;
        this.allOutgoingLines = allOutgoingLines;
    }


    public String getAllincominglines() {
        return allIncomingLines;
    }

    public void setAllincominglines(String allIncomingLines) {
        this.allIncomingLines = allIncomingLines;
    }
    public String getAlloutgoinglines() {
        return allOutgoingLines;
    }

    public void setAlloutgoinglines(String allOutgoingLines) {
        this.allOutgoingLines = allOutgoingLines;
    }


}