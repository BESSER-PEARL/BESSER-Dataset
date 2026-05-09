





import java.util.List;
import java.util.ArrayList;

public class mvc_Controller extends Annotable {

    private String name;





    private mvc_Component mvc_component;


    public mvc_Controller(
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

    public mvc_Component getMvc_component() {
        return mvc_component;
    }

    public void setMvc_component(mvc_Component mvc_component) {
        this.mvc_component = mvc_component;
    }

}