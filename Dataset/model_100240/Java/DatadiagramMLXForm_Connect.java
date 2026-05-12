





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLXForm_Connect  {

    private String fromPart;
    private String toCell;
    private String toSheet;
    private String toPart;
    private String fromCell;
    private String fromSheet;



    public DatadiagramMLXForm_Connect(
        String fromPart,        String toCell,        String toSheet,        String toPart,        String fromCell,        String fromSheet    ) {
        this.fromPart = fromPart;
        this.toCell = toCell;
        this.toSheet = toSheet;
        this.toPart = toPart;
        this.fromCell = fromCell;
        this.fromSheet = fromSheet;
    }


    public String getFrompart() {
        return fromPart;
    }

    public void setFrompart(String fromPart) {
        this.fromPart = fromPart;
    }
    public String getTocell() {
        return toCell;
    }

    public void setTocell(String toCell) {
        this.toCell = toCell;
    }
    public String getTosheet() {
        return toSheet;
    }

    public void setTosheet(String toSheet) {
        this.toSheet = toSheet;
    }
    public String getTopart() {
        return toPart;
    }

    public void setTopart(String toPart) {
        this.toPart = toPart;
    }
    public String getFromcell() {
        return fromCell;
    }

    public void setFromcell(String fromCell) {
        this.fromCell = fromCell;
    }
    public String getFromsheet() {
        return fromSheet;
    }

    public void setFromsheet(String fromSheet) {
        this.fromSheet = fromSheet;
    }


}