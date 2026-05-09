





import java.util.List;
import java.util.ArrayList;

public class efsm_Variable  {

    private String class_;
    private String type;
    private String name;





    private efsm_Input efsm_input;


    public efsm_Variable(
        String class_,        String type,        String name    ) {
        this.class_ = class_;
        this.type = type;
        this.name = name;
    }


    public String getClass_() {
        return class_;
    }

    public void setClass_(String class_) {
        this.class_ = class_;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public efsm_Input getEfsm_input() {
        return efsm_input;
    }

    public void setEfsm_input(efsm_Input efsm_input) {
        this.efsm_input = efsm_input;
    }

}