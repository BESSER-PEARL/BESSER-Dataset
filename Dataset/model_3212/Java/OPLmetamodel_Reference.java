





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_Reference extends Expression {

    private String name;





    private OPLmetamodel_Function oplmetamodel_function;




    private OPLmetamodel_Script oplmetamodel_script;


    public OPLmetamodel_Reference(
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

    public OPLmetamodel_Function getOplmetamodel_function() {
        return oplmetamodel_function;
    }

    public void setOplmetamodel_function(OPLmetamodel_Function oplmetamodel_function) {
        this.oplmetamodel_function = oplmetamodel_function;
    }
    public OPLmetamodel_Script getOplmetamodel_script() {
        return oplmetamodel_script;
    }

    public void setOplmetamodel_script(OPLmetamodel_Script oplmetamodel_script) {
        this.oplmetamodel_script = oplmetamodel_script;
    }

}