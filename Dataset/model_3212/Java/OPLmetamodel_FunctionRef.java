





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_FunctionRef  {

    private String name;





    private OPLmetamodel_Function oplmetamodel_function;


    public OPLmetamodel_FunctionRef(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public OPLmetamodel_Function getOplmetamodel_function() {
        return oplmetamodel_function;
    }

    public void setOplmetamodel_function(OPLmetamodel_Function oplmetamodel_function) {
        this.oplmetamodel_function = oplmetamodel_function;
    }

}