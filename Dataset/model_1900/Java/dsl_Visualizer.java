





import java.util.List;
import java.util.ArrayList;

public class dsl_Visualizer extends AbstractFrontElement, UIComponent {

    private String name;



    public dsl_Visualizer(
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


}