





import java.util.List;
import java.util.ArrayList;

public class model_CallCenterEmployee  {

    private String name;
    private None LOGGER;
    private int callsAnswered;
    private None employeeType;



    public model_CallCenterEmployee(
        String name,        None LOGGER,        int callsAnswered,        None employeeType    ) {
        this.name = name;
        this.LOGGER = LOGGER;
        this.callsAnswered = callsAnswered;
        this.employeeType = employeeType;
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
    public int getCallsanswered() {
        return callsAnswered;
    }

    public void setCallsanswered(int callsAnswered) {
        this.callsAnswered = callsAnswered;
    }
    public None getEmployeetype() {
        return employeeType;
    }

    public void setEmployeetype(None employeeType) {
        this.employeeType = employeeType;
    }


}