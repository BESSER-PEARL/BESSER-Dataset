





import java.util.List;
import java.util.ArrayList;

public class oCLlite_Import  {

    private String name;





    private oCLlite_Module ocllite_module;


    public oCLlite_Import(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public oCLlite_Module getOcllite_module() {
        return ocllite_module;
    }

    public void setOcllite_module(oCLlite_Module ocllite_module) {
        this.ocllite_module = ocllite_module;
    }

}