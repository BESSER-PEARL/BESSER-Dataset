





import java.util.List;
import java.util.ArrayList;

public class statesml_SystemUnitLibrary  {

    private String name;





    private statesml_SystemUnitModel statesml_systemunitmodel;


    public statesml_SystemUnitLibrary(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statesml_SystemUnitModel getStatesml_systemunitmodel() {
        return statesml_systemunitmodel;
    }

    public void setStatesml_systemunitmodel(statesml_SystemUnitModel statesml_systemunitmodel) {
        this.statesml_systemunitmodel = statesml_systemunitmodel;
    }

}