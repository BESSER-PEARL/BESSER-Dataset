





import java.util.List;
import java.util.ArrayList;

public class syswb103_FunctionProperty extends NamedElement {

    private String description;





    private syswb103_FunctionProperty syswb103_functionproperty;


    public syswb103_FunctionProperty(
        String description    ) {
        super(
        );
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public syswb103_FunctionProperty getSyswb103_functionproperty() {
        return syswb103_functionproperty;
    }

    public void setSyswb103_functionproperty(syswb103_FunctionProperty syswb103_functionproperty) {
        this.syswb103_functionproperty = syswb103_functionproperty;
    }

}