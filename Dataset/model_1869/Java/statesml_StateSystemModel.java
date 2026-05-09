





import java.util.List;
import java.util.ArrayList;

public class statesml_StateSystemModel  {

    private String name;





    private statesml_SystemUnit statesml_systemunit;


    public statesml_StateSystemModel(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statesml_SystemUnit getStatesml_systemunit() {
        return statesml_systemunit;
    }

    public void setStatesml_systemunit(statesml_SystemUnit statesml_systemunit) {
        this.statesml_systemunit = statesml_systemunit;
    }

}