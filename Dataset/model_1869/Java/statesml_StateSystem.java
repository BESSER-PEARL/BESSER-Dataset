





import java.util.List;
import java.util.ArrayList;

public class statesml_StateSystem  {






    private List<statesml_Attribute> statesml_attributes;




    private statesml_StateSystemModel statesml_statesystemmodel;


    public statesml_StateSystem(
    ) {
        this.statesml_attributes = new ArrayList<>();
    }

    public statesml_StateSystem(
        ArrayList<statesml_Attribute> statesml_attributes    ) {
        this.statesml_attributes = statesml_attributes;
    }


    public List<statesml_Attribute> getStatesml_attributes() {
        return statesml_attributes;
    }

    public void addStatesml_attribute(Statesml_attribute statesml_attribute) {
        this.statesml_attributes.add(statesml_attribute);
    }
    public statesml_StateSystemModel getStatesml_statesystemmodel() {
        return statesml_statesystemmodel;
    }

    public void setStatesml_statesystemmodel(statesml_StateSystemModel statesml_statesystemmodel) {
        this.statesml_statesystemmodel = statesml_statesystemmodel;
    }

}