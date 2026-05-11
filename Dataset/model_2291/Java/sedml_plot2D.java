





import java.util.List;
import java.util.ArrayList;

public class sedml_plot2D  {

    private String name;
    private String id;





    private sedml_listOfOutputs sedml_listofoutputs;


    public sedml_plot2D(
        String name,        String id    ) {
        this.name = name;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public sedml_listOfOutputs getSedml_listofoutputs() {
        return sedml_listofoutputs;
    }

    public void setSedml_listofoutputs(sedml_listOfOutputs sedml_listofoutputs) {
        this.sedml_listofoutputs = sedml_listofoutputs;
    }

}