





import java.util.List;
import java.util.ArrayList;

public class model_AbstractType  {

    private String name;





    private model_AbstractType model_abstracttype;




    private model_Container model_container;


    public model_AbstractType(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public model_AbstractType getModel_abstracttype() {
        return model_abstracttype;
    }

    public void setModel_abstracttype(model_AbstractType model_abstracttype) {
        this.model_abstracttype = model_abstracttype;
    }
    public model_Container getModel_container() {
        return model_container;
    }

    public void setModel_container(model_Container model_container) {
        this.model_container = model_container;
    }

}