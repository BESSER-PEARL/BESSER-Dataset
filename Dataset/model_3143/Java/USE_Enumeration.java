





import java.util.List;
import java.util.ArrayList;

public class USE_Enumeration  {

    private String name;





    private USE_EnumerationType use_enumerationtype;




    private USE_Model use_model;


    public USE_Enumeration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public USE_EnumerationType getUse_enumerationtype() {
        return use_enumerationtype;
    }

    public void setUse_enumerationtype(USE_EnumerationType use_enumerationtype) {
        this.use_enumerationtype = use_enumerationtype;
    }
    public USE_Model getUse_model() {
        return use_model;
    }

    public void setUse_model(USE_Model use_model) {
        this.use_model = use_model;
    }

}