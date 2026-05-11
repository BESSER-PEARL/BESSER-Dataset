





import java.util.List;
import java.util.ArrayList;

public class data_Variable  {

    private String id;





    private data_Variables data_variables;


    public data_Variable(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public data_Variables getData_variables() {
        return data_variables;
    }

    public void setData_variables(data_Variables data_variables) {
        this.data_variables = data_variables;
    }

}