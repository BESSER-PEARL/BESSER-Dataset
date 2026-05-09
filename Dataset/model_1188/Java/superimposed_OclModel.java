





import java.util.List;
import java.util.ArrayList;

public class superimposed_OclModel  {

    private String name;





    private superimposed_OclModelElement superimposed_oclmodelelement;


    public superimposed_OclModel(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public superimposed_OclModelElement getSuperimposed_oclmodelelement() {
        return superimposed_oclmodelelement;
    }

    public void setSuperimposed_oclmodelelement(superimposed_OclModelElement superimposed_oclmodelelement) {
        this.superimposed_oclmodelelement = superimposed_oclmodelelement;
    }

}