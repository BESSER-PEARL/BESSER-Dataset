





import java.util.List;
import java.util.ArrayList;

public class sedml_dataGenerator  {

    private String id;
    private String name;





    private sedml_listOfDataGenerators sedml_listofdatagenerators;


    public sedml_dataGenerator(
        String id,        String name    ) {
        this.id = id;
        this.name = name;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sedml_listOfDataGenerators getSedml_listofdatagenerators() {
        return sedml_listofdatagenerators;
    }

    public void setSedml_listofdatagenerators(sedml_listOfDataGenerators sedml_listofdatagenerators) {
        this.sedml_listofdatagenerators = sedml_listofdatagenerators;
    }

}