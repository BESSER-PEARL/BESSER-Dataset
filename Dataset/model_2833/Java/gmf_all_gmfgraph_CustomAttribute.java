





import java.util.List;
import java.util.ArrayList;

public class gmf_all_gmfgraph_CustomAttribute  {

    private String value;
    private boolean directAccess;
    private String name;
    private boolean multiStatementValue;



    public gmf_all_gmfgraph_CustomAttribute(
        String value,        boolean directAccess,        String name,        boolean multiStatementValue    ) {
        this.value = value;
        this.directAccess = directAccess;
        this.name = name;
        this.multiStatementValue = multiStatementValue;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public boolean getDirectaccess() {
        return directAccess;
    }

    public void setDirectaccess(boolean directAccess) {
        this.directAccess = directAccess;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getMultistatementvalue() {
        return multiStatementValue;
    }

    public void setMultistatementvalue(boolean multiStatementValue) {
        this.multiStatementValue = multiStatementValue;
    }


}