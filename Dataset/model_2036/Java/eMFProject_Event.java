





import java.util.List;
import java.util.ArrayList;

public class eMFProject_Event  {

    private String name;
    private String code;





    private eMFProject_Statemachine emfproject_statemachine;




    private eMFProject_Transition emfproject_transition;




    private eMFProject_Statemachine emfproject_statemachine;


    public eMFProject_Event(
        String name,        String code    ) {
        this.name = name;
        this.code = code;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public eMFProject_Statemachine getEmfproject_statemachine() {
        return emfproject_statemachine;
    }

    public void setEmfproject_statemachine(eMFProject_Statemachine emfproject_statemachine) {
        this.emfproject_statemachine = emfproject_statemachine;
    }
    public eMFProject_Transition getEmfproject_transition() {
        return emfproject_transition;
    }

    public void setEmfproject_transition(eMFProject_Transition emfproject_transition) {
        this.emfproject_transition = emfproject_transition;
    }
    public eMFProject_Statemachine getEmfproject_statemachine() {
        return emfproject_statemachine;
    }

    public void setEmfproject_statemachine(eMFProject_Statemachine emfproject_statemachine) {
        this.emfproject_statemachine = emfproject_statemachine;
    }

}