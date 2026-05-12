





import java.util.List;
import java.util.ArrayList;

public class fowlerdsl_Command  {

    private String code;
    private String name;





    private fowlerdsl_Statemachine fowlerdsl_statemachine;


    public fowlerdsl_Command(
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

    public fowlerdsl_Statemachine getFowlerdsl_statemachine() {
        return fowlerdsl_statemachine;
    }

    public void setFowlerdsl_statemachine(fowlerdsl_Statemachine fowlerdsl_statemachine) {
        this.fowlerdsl_statemachine = fowlerdsl_statemachine;
    }

}