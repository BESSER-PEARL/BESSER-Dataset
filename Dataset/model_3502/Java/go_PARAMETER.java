





import java.util.List;
import java.util.ArrayList;

public class go_PARAMETER  {

    private String id;





    private go_LITERAIS_BASICOS go_literais_basicos;




    private go_PARAMETERS_LIST go_parameters_list;


    public go_PARAMETER(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public go_LITERAIS_BASICOS getGo_literais_basicos() {
        return go_literais_basicos;
    }

    public void setGo_literais_basicos(go_LITERAIS_BASICOS go_literais_basicos) {
        this.go_literais_basicos = go_literais_basicos;
    }
    public go_PARAMETERS_LIST getGo_parameters_list() {
        return go_parameters_list;
    }

    public void setGo_parameters_list(go_PARAMETERS_LIST go_parameters_list) {
        this.go_parameters_list = go_parameters_list;
    }

}