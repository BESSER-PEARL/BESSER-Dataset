





import java.util.List;
import java.util.ArrayList;

public class cmof_ValueSpecification extends TypedElement, PackageableElement {






    private cmof_Property cmof_property;




    private cmof_Parameter cmof_parameter;


    public cmof_ValueSpecification(
    ) {
        super(
        );
    }



    public cmof_Property getCmof_property() {
        return cmof_property;
    }

    public void setCmof_property(cmof_Property cmof_property) {
        this.cmof_property = cmof_property;
    }
    public cmof_Parameter getCmof_parameter() {
        return cmof_parameter;
    }

    public void setCmof_parameter(cmof_Parameter cmof_parameter) {
        this.cmof_parameter = cmof_parameter;
    }

}