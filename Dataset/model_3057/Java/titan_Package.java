





import java.util.List;
import java.util.ArrayList;

public class titan_Package  {

    private String name;





    private titan_Module titan_module;


    public titan_Package(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public titan_Module getTitan_module() {
        return titan_module;
    }

    public void setTitan_module(titan_Module titan_module) {
        this.titan_module = titan_module;
    }

}