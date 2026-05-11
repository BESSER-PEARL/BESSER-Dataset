





import java.util.List;
import java.util.ArrayList;

public class forms_EnumerationType  {

    private String name;





    private forms_EntityModel forms_entitymodel;


    public forms_EnumerationType(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public forms_EntityModel getForms_entitymodel() {
        return forms_entitymodel;
    }

    public void setForms_entitymodel(forms_EntityModel forms_entitymodel) {
        this.forms_entitymodel = forms_entitymodel;
    }

}