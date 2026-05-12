





import java.util.List;
import java.util.ArrayList;

public class newP_Requirement  {

    private String identifier;
    private String name;
    private boolean mandatory;
    private int priority;



    public newP_Requirement(
        String identifier,        String name,        boolean mandatory,        int priority    ) {
        this.identifier = identifier;
        this.name = name;
        this.mandatory = mandatory;
        this.priority = priority;
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
    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }
    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }


}