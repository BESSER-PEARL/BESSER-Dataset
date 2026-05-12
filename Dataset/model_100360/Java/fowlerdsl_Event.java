





import java.util.List;
import java.util.ArrayList;

public class fowlerdsl_Event  {

    private String name;
    private boolean resetting;
    private String code;





    private fowlerdsl_Statemachine fowlerdsl_statemachine;


    public fowlerdsl_Event(
        String name,        boolean resetting,        String code    ) {
        this.name = name;
        this.resetting = resetting;
        this.code = code;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getResetting() {
        return resetting;
    }

    public void setResetting(boolean resetting) {
        this.resetting = resetting;
    }
    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public fowlerdsl_Statemachine getFowlerdsl_statemachine() {
        return fowlerdsl_statemachine;
    }

    public void setFowlerdsl_statemachine(fowlerdsl_Statemachine fowlerdsl_statemachine) {
        this.fowlerdsl_statemachine = fowlerdsl_statemachine;
    }

}