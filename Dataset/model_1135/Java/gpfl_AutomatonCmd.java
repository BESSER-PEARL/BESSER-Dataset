





import java.util.List;
import java.util.ArrayList;

public class gpfl_AutomatonCmd extends GExpression {

    private String name;





    private gpfl_AutomataDef gpfl_automatadef;


    public gpfl_AutomatonCmd(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public gpfl_AutomataDef getGpfl_automatadef() {
        return gpfl_automatadef;
    }

    public void setGpfl_automatadef(gpfl_AutomataDef gpfl_automatadef) {
        this.gpfl_automatadef = gpfl_automatadef;
    }

}