





import java.util.List;
import java.util.ArrayList;

public class mvc_View extends Annotable {

    private String name;





    private mvc_ControllerView mvc_controllerview;


    public mvc_View(
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

    public mvc_ControllerView getMvc_controllerview() {
        return mvc_controllerview;
    }

    public void setMvc_controllerview(mvc_ControllerView mvc_controllerview) {
        this.mvc_controllerview = mvc_controllerview;
    }

}