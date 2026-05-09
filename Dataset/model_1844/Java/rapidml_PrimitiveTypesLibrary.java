





import java.util.List;
import java.util.ArrayList;

public class rapidml_PrimitiveTypesLibrary  {

    private String name;





    private rapidml_ZenModel rapidml_zenmodel;


    public rapidml_PrimitiveTypesLibrary(
        String name    ) {
        this.name = name;
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

}