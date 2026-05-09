





import java.util.List;
import java.util.ArrayList;

public class UML2_PrimitiveFunction extends PackageableElement {

    private String body;
    private String language;





    private UML2_ApplyFunctionAction uml2_applyfunctionaction;


    public UML2_PrimitiveFunction(
        String body,        String language    ) {
        super(
        );
        this.body = body;
        this.language = language;
    }


    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public UML2_ApplyFunctionAction getUml2_applyfunctionaction() {
        return uml2_applyfunctionaction;
    }

    public void setUml2_applyfunctionaction(UML2_ApplyFunctionAction uml2_applyfunctionaction) {
        this.uml2_applyfunctionaction = uml2_applyfunctionaction;
    }

}