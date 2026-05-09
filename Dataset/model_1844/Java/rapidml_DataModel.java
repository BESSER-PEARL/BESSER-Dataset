





import java.util.List;
import java.util.ArrayList;

public class rapidml_DataModel extends Documentable, HasTitle {

    private String name;





    private rapidml_ZenModel rapidml_zenmodel;




    private List<rapidml_DataType> rapidml_datatypes;




    private rapidml_ResourceAPI rapidml_resourceapi;


    public rapidml_DataModel(
        String name    ) {
        super(
        );
        this.name = name;
        this.rapidml_datatypes = new ArrayList<>();
    }

    public rapidml_DataModel(
        String name        ArrayList<rapidml_DataType> rapidml_datatypes    ) {
        this.name = name;
        this.rapidml_datatypes = rapidml_datatypes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public rapidml_ZenModel getRapidml_zenmodel() {
        return rapidml_zenmodel;
    }

    public void setRapidml_zenmodel(rapidml_ZenModel rapidml_zenmodel) {
        this.rapidml_zenmodel = rapidml_zenmodel;
    }
    public List<rapidml_DataType> getRapidml_datatypes() {
        return rapidml_datatypes;
    }

    public void addRapidml_datatype(Rapidml_datatype rapidml_datatype) {
        this.rapidml_datatypes.add(rapidml_datatype);
    }
    public rapidml_ResourceAPI getRapidml_resourceapi() {
        return rapidml_resourceapi;
    }

    public void setRapidml_resourceapi(rapidml_ResourceAPI rapidml_resourceapi) {
        this.rapidml_resourceapi = rapidml_resourceapi;
    }

}