





import java.util.List;
import java.util.ArrayList;

public class uma_MethodElementProperty extends PackageableElement {

    private String value;





    private uma_MethodElement uma_methodelement;


    public uma_MethodElementProperty(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public uma_MethodElement getUma_methodelement() {
        return uma_methodelement;
    }

    public void setUma_methodelement(uma_MethodElement uma_methodelement) {
        this.uma_methodelement = uma_methodelement;
    }

}