





import java.util.List;
import java.util.ArrayList;

public class model_CallCenterEmployee  {

    private int callsAnswered;
    private String name;
    private None LOGGER;
    private String employeeType;



    public model_CallCenterEmployee(
        int callsAnswered,        String name,        None LOGGER,        String employeeType    ) {
        this.callsAnswered = callsAnswered;
        this.name = name;
        this.LOGGER = LOGGER;
        this.employeeType = employeeType;
    }


    public int getCallsanswered() {
        return callsAnswered;
    }

    public void setCallsanswered(int callsAnswered) {
        this.callsAnswered = callsAnswered;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public None getLogger() {
        return LOGGER;
    }

    public void setLogger(None LOGGER) {
        this.LOGGER = LOGGER;
    }
    public String getEmployeetype() {
        return employeeType;
    }

    public void setEmployeetype(String employeeType) {
        this.employeeType = employeeType;
    }


}