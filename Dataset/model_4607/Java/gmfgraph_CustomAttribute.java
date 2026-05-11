





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_CustomAttribute  {

    private boolean directAccess;
    private boolean multiStatementValue;
    private String name;
    private String value;





    private gmfgraph_CustomAttributeOwner gmfgraph_customattributeowner;


    public gmfgraph_CustomAttribute(
        boolean directAccess,        boolean multiStatementValue,        String name,        String value    ) {
        this.directAccess = directAccess;
        this.multiStatementValue = multiStatementValue;
        this.name = name;
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

    public gmfgraph_CustomAttributeOwner getGmfgraph_customattributeowner() {
        return gmfgraph_customattributeowner;
    }

    public void setGmfgraph_customattributeowner(gmfgraph_CustomAttributeOwner gmfgraph_customattributeowner) {
        this.gmfgraph_customattributeowner = gmfgraph_customattributeowner;
    }

}