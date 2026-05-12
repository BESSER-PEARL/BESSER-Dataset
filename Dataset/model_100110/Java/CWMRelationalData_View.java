





import java.util.List;
import java.util.ArrayList;

public class CWMRelationalData_View extends NamedColumnSet {

    private String checkOption;
    private String isReadOnly;



    public CWMRelationalData_View(
        String checkOption,        String isReadOnly    ) {
        super(
        );
        this.checkOption = checkOption;
        this.isReadOnly = isReadOnly;
    }


    public String getCheckoption() {
        return checkOption;
    }

    public void setCheckoption(String checkOption) {
        this.checkOption = checkOption;
    }
    public String getIsreadonly() {
        return isReadOnly;
    }

    public void setIsreadonly(String isReadOnly) {
        this.isReadOnly = isReadOnly;
    }


}