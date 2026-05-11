





import java.util.List;
import java.util.ArrayList;

public class iotw_StateComponent extends Component {

    private String name;





    private iotw_StateSchema iotw_stateschema;


    public iotw_StateComponent(
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

    public iotw_StateSchema getIotw_stateschema() {
        return iotw_stateschema;
    }

    public void setIotw_stateschema(iotw_StateSchema iotw_stateschema) {
        this.iotw_stateschema = iotw_stateschema;
    }

}