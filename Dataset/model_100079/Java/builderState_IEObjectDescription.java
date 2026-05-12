





import java.util.List;
import java.util.ArrayList;

public class builderState_IEObjectDescription  {

    private String name;





    private builderState_ResourceDescription builderstate_resourcedescription;


    public builderState_IEObjectDescription(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public builderState_ResourceDescription getBuilderstate_resourcedescription() {
        return builderstate_resourcedescription;
    }

    public void setBuilderstate_resourcedescription(builderState_ResourceDescription builderstate_resourcedescription) {
        this.builderstate_resourcedescription = builderstate_resourcedescription;
    }

}