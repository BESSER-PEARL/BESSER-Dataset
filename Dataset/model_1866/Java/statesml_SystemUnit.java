





import java.util.List;
import java.util.ArrayList;

public class statesml_SystemUnit  {

    private String name;





    private statesml_StatesMLModel statesml_statesmlmodel;


    public statesml_SystemUnit(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statesml_StatesMLModel getStatesml_statesmlmodel() {
        return statesml_statesmlmodel;
    }

    public void setStatesml_statesmlmodel(statesml_StatesMLModel statesml_statesmlmodel) {
        this.statesml_statesmlmodel = statesml_statesmlmodel;
    }

}