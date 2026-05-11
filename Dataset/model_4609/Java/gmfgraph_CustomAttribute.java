





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_CustomAttribute  {

    private String name;
    private String value;
    private boolean directAccess;
    private boolean multiStatementValue;



    public gmfgraph_CustomAttribute(
        String name,        String value,        boolean directAccess,        boolean multiStatementValue    ) {
        this.name = name;
        this.value = value;
        this.directAccess = directAccess;
        this.multiStatementValue = multiStatementValue;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public boolean getMultistatementvalue() {
        return multiStatementValue;
    }

    public void setMultistatementvalue(boolean multiStatementValue) {
        this.multiStatementValue = multiStatementValue;
    }


}