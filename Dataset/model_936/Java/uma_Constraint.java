





import java.util.List;
import java.util.ArrayList;

public class uma_Constraint extends MethodElement {

    private String mainDescription;





    private uma_MethodElement uma_methodelement;


    public uma_Constraint(
        String mainDescription    ) {
        super(
        );
        this.mainDescription = mainDescription;
    }


    public String getMaindescription() {
        return mainDescription;
    }

    public void setMaindescription(String mainDescription) {
        this.mainDescription = mainDescription;
    }

    public uma_MethodElement getUma_methodelement() {
        return uma_methodelement;
    }

    public void setUma_methodelement(uma_MethodElement uma_methodelement) {
        this.uma_methodelement = uma_methodelement;
    }

}