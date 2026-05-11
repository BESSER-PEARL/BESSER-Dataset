





import java.util.List;
import java.util.ArrayList;

public class behavioral_status_and_action_old_SAMStatusVariable  {

    private String name;
    private boolean isAgentVariable;





    private SapClass sapclass;


    public behavioral_status_and_action_old_SAMStatusVariable(
        String name,        boolean isAgentVariable    ) {
        this.name = name;
        this.isAgentVariable = isAgentVariable;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsagentvariable() {
        return isAgentVariable;
    }

    public void setIsagentvariable(boolean isAgentVariable) {
        this.isAgentVariable = isAgentVariable;
    }

    public SapClass getSapclass() {
        return sapclass;
    }

    public void setSapclass(SapClass sapclass) {
        this.sapclass = sapclass;
    }

}