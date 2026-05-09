





import java.util.List;
import java.util.ArrayList;

public class uma_Constraint extends MethodElement {

    private String body;





    private uma_MethodElement uma_methodelement;


    public uma_Constraint(
        String body    ) {
        super(
        );
        this.body = body;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public uma_MethodElement getUma_methodelement() {
        return uma_methodelement;
    }

    public void setUma_methodelement(uma_MethodElement uma_methodelement) {
        this.uma_methodelement = uma_methodelement;
    }

}