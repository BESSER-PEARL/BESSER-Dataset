





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLTextFormat_Connect  {

    private String toPart;
    private String toSheet;
    private String fromPart;
    private String fromCell;
    private String toCell;
    private String fromSheet;



    public DatadiagramMLTextFormat_Connect(
        String toPart,        String toSheet,        String fromPart,        String fromCell,        String toCell,        String fromSheet    ) {
        this.toPart = toPart;
        this.toSheet = toSheet;
        this.fromPart = fromPart;
        this.fromCell = fromCell;
        this.toCell = toCell;
        this.fromSheet = fromSheet;
    }


    public String getTopart() {
        return toPart;
    }

    public void setTopart(String toPart) {
        this.toPart = toPart;
    }
    public String getTosheet() {
        return toSheet;
    }

    public void setTosheet(String toSheet) {
        this.toSheet = toSheet;
    }
    public String getFrompart() {
        return fromPart;
    }

    public void setFrompart(String fromPart) {
        this.fromPart = fromPart;
    }
    public String getFromcell() {
        return fromCell;
    }

    public void setFromcell(String fromCell) {
        this.fromCell = fromCell;
    }
    public String getTocell() {
        return toCell;
    }

    public void setTocell(String toCell) {
        this.toCell = toCell;
    }
    public String getFromsheet() {
        return fromSheet;
    }

    public void setFromsheet(String fromSheet) {
        this.fromSheet = fromSheet;
    }


}