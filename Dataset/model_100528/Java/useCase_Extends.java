





import java.util.List;
import java.util.ArrayList;

public class useCase_Extends  {

    private String name;
    private String rules;



    public useCase_Extends(
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