





import java.util.List;
import java.util.ArrayList;

public class myDsl_Layer  {

    private String name;





    private myDsl_Component mydsl_component;


    public myDsl_Layer(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_Component getMydsl_component() {
        return mydsl_component;
    }

    public void setMydsl_component(myDsl_Component mydsl_component) {
        this.mydsl_component = mydsl_component;
    }

}