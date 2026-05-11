





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_CustomAttribute  {

    private boolean multiStatementValue;
    private String value;
    private String name;
    private boolean directAccess;





    private gmfgraph_CustomClass gmfgraph_customclass;


    public gmfgraph_CustomAttribute(
        boolean multiStatementValue,        String value,        String name,        boolean directAccess    ) {
        this.multiStatementValue = multiStatementValue;
        this.value = value;
        this.name = name;
        this.directAccess = directAccess;
    }


    public boolean getMultistatementvalue() {
        return multiStatementValue;
    }

    public void setMultistatementvalue(boolean multiStatementValue) {
        this.multiStatementValue = multiStatementValue;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getDirectaccess() {
        return directAccess;
    }

    public void setDirectaccess(boolean directAccess) {
        this.directAccess = directAccess;
    }

    public gmfgraph_CustomClass getGmfgraph_customclass() {
        return gmfgraph_customclass;
    }

    public void setGmfgraph_customclass(gmfgraph_CustomClass gmfgraph_customclass) {
        this.gmfgraph_customclass = gmfgraph_customclass;
    }

}