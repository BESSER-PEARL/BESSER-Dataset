





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_ClassifierTemplateParameter extends TemplateParameter {

    private boolean allowSubstitutable;



    public UML2WithID_ClassifierTemplateParameter(
        boolean allowSubstitutable    ) {
        super(
        );
        this.allowSubstitutable = allowSubstitutable;
    }


    public boolean getAllowsubstitutable() {
        return allowSubstitutable;
    }

    public void setAllowsubstitutable(boolean allowSubstitutable) {
        this.allowSubstitutable = allowSubstitutable;
    }


}