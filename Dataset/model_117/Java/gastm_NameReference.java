





import java.util.List;
import java.util.ArrayList;

public class gastm_NameReference extends Expression {






    private gastm_Name gastm_name;




    private gastm_DefinitionObject gastm_definitionobject;


    public gastm_NameReference(
    ) {
        super(
        );
    }



    public gastm_Name getGastm_name() {
        return gastm_name;
    }

    public void setGastm_name(gastm_Name gastm_name) {
        this.gastm_name = gastm_name;
    }
    public gastm_DefinitionObject getGastm_definitionobject() {
        return gastm_definitionobject;
    }

    public void setGastm_definitionobject(gastm_DefinitionObject gastm_definitionobject) {
        this.gastm_definitionobject = gastm_definitionobject;
    }

}