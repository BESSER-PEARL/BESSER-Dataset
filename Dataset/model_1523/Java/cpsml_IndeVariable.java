





import java.util.List;
import java.util.ArrayList;

public class cpsml_IndeVariable  {

    private String name;





    private cpsml_Function cpsml_function;


    public cpsml_IndeVariable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cpsml_Function getCpsml_function() {
        return cpsml_function;
    }

    public void setCpsml_function(cpsml_Function cpsml_function) {
        this.cpsml_function = cpsml_function;
    }

}