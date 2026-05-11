





import java.util.List;
import java.util.ArrayList;

public class service_template_AbstractProcessModel extends IOEP {

    private String name;



    public service_template_AbstractProcessModel(
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