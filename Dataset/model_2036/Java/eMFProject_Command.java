





import java.util.List;
import java.util.ArrayList;

public class eMFProject_Command  {

    private String code;
    private String name;





    private eMFProject_Statemachine emfproject_statemachine;


    public eMFProject_Command(
        String code,        String name    ) {
        this.code = code;
        this.name = name;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public eMFProject_Statemachine getEmfproject_statemachine() {
        return emfproject_statemachine;
    }

    public void setEmfproject_statemachine(eMFProject_Statemachine emfproject_statemachine) {
        this.emfproject_statemachine = emfproject_statemachine;
    }

}