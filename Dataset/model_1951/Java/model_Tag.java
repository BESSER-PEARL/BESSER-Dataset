





import java.util.List;
import java.util.ArrayList;

public class model_Tag extends ISynchable {

    private String name;





    private model_GeppettoModel model_geppettomodel;




    private model_Tag model_tag;


    public model_Tag(
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

    public model_GeppettoModel getModel_geppettomodel() {
        return model_geppettomodel;
    }

    public void setModel_geppettomodel(model_GeppettoModel model_geppettomodel) {
        this.model_geppettomodel = model_geppettomodel;
    }
    public model_Tag getModel_tag() {
        return model_tag;
    }

    public void setModel_tag(model_Tag model_tag) {
        this.model_tag = model_tag;
    }

}