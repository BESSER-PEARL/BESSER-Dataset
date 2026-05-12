





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLBasicDef_Connect  {

    private String fromCell;
    private String toPart;
    private String fromPart;
    private String fromSheet;
    private String toSheet;
    private String toCell;



    public DatadiagramMLBasicDef_Connect(
        String fromCell,        String toPart,        String fromPart,        String fromSheet,        String toSheet,        String toCell    ) {
        this.fromCell = fromCell;
        this.toPart = toPart;
        this.fromPart = fromPart;
        this.fromSheet = fromSheet;
        this.toSheet = toSheet;
        this.toCell = toCell;
    }


    public String getFromcell() {
        return fromCell;
    }

    public void setFromcell(String fromCell) {
        this.fromCell = fromCell;
    }
    public String getTopart() {
        return toPart;
    }

    public void setTopart(String toPart) {
        this.toPart = toPart;
    }
    public String getFrompart() {
        return fromPart;
    }

    public void setFrompart(String fromPart) {
        this.fromPart = fromPart;
    }
    public String getFromsheet() {
        return fromSheet;
    }

    public void setFromsheet(String fromSheet) {
        this.fromSheet = fromSheet;
    }
    public String getTosheet() {
        return toSheet;
    }

    public void setTosheet(String toSheet) {
        this.toSheet = toSheet;
    }
    public String getTocell() {
        return toCell;
    }

    public void setTocell(String toCell) {
        this.toCell = toCell;
    }


}