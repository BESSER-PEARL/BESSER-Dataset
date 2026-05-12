





import java.util.List;
import java.util.ArrayList;

public class requirements_editor_Requirement  {

    private int priority;
    private boolean isMandatory;
    private String identifier;
    private String name;



    public requirements_editor_Requirement(
        int priority,        boolean isMandatory,        String identifier,        String name    ) {
        this.priority = priority;
        this.isMandatory = isMandatory;
        this.identifier = identifier;
        this.name = name;
    }


    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }
    public boolean getIsmandatory() {
        return isMandatory;
    }

    public void setIsmandatory(boolean isMandatory) {
        this.isMandatory = isMandatory;
    }
    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}