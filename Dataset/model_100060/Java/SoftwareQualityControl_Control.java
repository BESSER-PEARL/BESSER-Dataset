





import java.util.List;
import java.util.ArrayList;

public class SoftwareQualityControl_Control  {

    private String eltRef;
    private String controlledElt;
    private String formRef;
    private String developmentPhase;
    private String responsible;
    private String eltAuthor;
    private String component;
    private String scope;



    public SoftwareQualityControl_Control(
        String eltRef,        String controlledElt,        String formRef,        String developmentPhase,        String responsible,        String eltAuthor,        String component,        String scope    ) {
        this.eltRef = eltRef;
        this.controlledElt = controlledElt;
        this.formRef = formRef;
        this.developmentPhase = developmentPhase;
        this.responsible = responsible;
        this.eltAuthor = eltAuthor;
        this.component = component;
        this.scope = scope;
    }


    public String getEltref() {
        return eltRef;
    }

    public void setEltref(String eltRef) {
        this.eltRef = eltRef;
    }
    public String getControlledelt() {
        return controlledElt;
    }

    public void setControlledelt(String controlledElt) {
        this.controlledElt = controlledElt;
    }
    public String getFormref() {
        return formRef;
    }

    public void setFormref(String formRef) {
        this.formRef = formRef;
    }
    public String getDevelopmentphase() {
        return developmentPhase;
    }

    public void setDevelopmentphase(String developmentPhase) {
        this.developmentPhase = developmentPhase;
    }
    public String getResponsible() {
        return responsible;
    }

    public void setResponsible(String responsible) {
        this.responsible = responsible;
    }
    public String getEltauthor() {
        return eltAuthor;
    }

    public void setEltauthor(String eltAuthor) {
        this.eltAuthor = eltAuthor;
    }
    public String getComponent() {
        return component;
    }

    public void setComponent(String component) {
        this.component = component;
    }
    public String getScope() {
        return scope;
    }

    public void setScope(String scope) {
        this.scope = scope;
    }


}