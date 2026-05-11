





import java.util.List;
import java.util.ArrayList;

public class langc_Function extends NamedElement {

    private String linkage;





    private langc_ElementReference langc_elementreference;




    private langc_FunctionImplementation langc_functionimplementation;




    private langc_FunctionImplementation langc_functionimplementation;


    public langc_Function(
        String linkage    ) {
        super(
        );
        this.linkage = linkage;
    }


    public String getLinkage() {
        return linkage;
    }

    public void setLinkage(String linkage) {
        this.linkage = linkage;
    }

    public langc_ElementReference getLangc_elementreference() {
        return langc_elementreference;
    }

    public void setLangc_elementreference(langc_ElementReference langc_elementreference) {
        this.langc_elementreference = langc_elementreference;
    }
    public langc_FunctionImplementation getLangc_functionimplementation() {
        return langc_functionimplementation;
    }

    public void setLangc_functionimplementation(langc_FunctionImplementation langc_functionimplementation) {
        this.langc_functionimplementation = langc_functionimplementation;
    }
    public langc_FunctionImplementation getLangc_functionimplementation() {
        return langc_functionimplementation;
    }

    public void setLangc_functionimplementation(langc_FunctionImplementation langc_functionimplementation) {
        this.langc_functionimplementation = langc_functionimplementation;
    }

}