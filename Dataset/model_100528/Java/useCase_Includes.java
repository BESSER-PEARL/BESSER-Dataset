





import java.util.List;
import java.util.ArrayList;

public class useCase_Includes  {

    private String name;
    private String rules;



    public useCase_Includes(
        String name,        String rules    ) {
        this.name = name;
        this.rules = rules;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRules() {
        return rules;
    }

    public void setRules(String rules) {
        this.rules = rules;
    }


}