





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_CustomAttribute  {

    private String value;
    private boolean multiStatementValue;
    private boolean directAccess;
    private String name;





    private gmfgraph_CustomClass gmfgraph_customclass;


    public gmfgraph_CustomAttribute(
        String value,        boolean multiStatementValue,        boolean directAccess,        String name    ) {
        this.value = value;
        this.multiStatementValue = multiStatementValue;
        this.directAccess = directAccess;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public boolean getMultistatementvalue() {
        return multiStatementValue;
    }

    public void setMultistatementvalue(boolean multiStatementValue) {
        this.multiStatementValue = multiStatementValue;
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

    public gmfgraph_CustomClass getGmfgraph_customclass() {
        return gmfgraph_customclass;
    }

    public void setGmfgraph_customclass(gmfgraph_CustomClass gmfgraph_customclass) {
        this.gmfgraph_customclass = gmfgraph_customclass;
    }

}