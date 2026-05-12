





import java.util.List;
import java.util.ArrayList;

public class oracle_DatabaseModuleExtensibleProperty extends ExtensibleModel {

    private String bizPkg;
    private String tableType;
    private String startDate;
    private String splitNum;
    private String space;
    private String splitField;



    public oracle_DatabaseModuleExtensibleProperty(
        String bizPkg,        String tableType,        String startDate,        String splitNum,        String space,        String splitField    ) {
        super(
        );
        this.bizPkg = bizPkg;
        this.tableType = tableType;
        this.startDate = startDate;
        this.splitNum = splitNum;
        this.space = space;
        this.splitField = splitField;
    }


    public String getBizpkg() {
        return bizPkg;
    }

    public void setBizpkg(String bizPkg) {
        this.bizPkg = bizPkg;
    }
    public String getTabletype() {
        return tableType;
    }

    public void setTabletype(String tableType) {
        this.tableType = tableType;
    }
    public String getStartdate() {
        return startDate;
    }

    public void setStartdate(String startDate) {
        this.startDate = startDate;
    }
    public String getSplitnum() {
        return splitNum;
    }

    public void setSplitnum(String splitNum) {
        this.splitNum = splitNum;
    }
    public String getSpace() {
        return space;
    }

    public void setSpace(String space) {
        this.space = space;
    }
    public String getSplitfield() {
        return splitField;
    }

    public void setSplitfield(String splitField) {
        this.splitField = splitField;
    }


}