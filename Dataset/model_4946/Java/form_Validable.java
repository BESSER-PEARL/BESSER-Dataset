





import java.util.List;
import java.util.ArrayList;

public class form_Validable  {

    private boolean below;
    private String useDefaultValidator;





    private List<form_Validator> form_validators;


    public form_Validable(
        boolean below,        String useDefaultValidator    ) {
        this.below = below;
        this.useDefaultValidator = useDefaultValidator;
        this.form_validators = new ArrayList<>();
    }

    public form_Validable(
        boolean below,        String useDefaultValidator        ArrayList<form_Validator> form_validators    ) {
        this.below = below;
        this.useDefaultValidator = useDefaultValidator;
        this.form_validators = form_validators;
    }

    public boolean getBelow() {
        return below;
    }

    public void setBelow(boolean below) {
        this.below = below;
    }
    public String getUsedefaultvalidator() {
        return useDefaultValidator;
    }

    public void setUsedefaultvalidator(String useDefaultValidator) {
        this.useDefaultValidator = useDefaultValidator;
    }

    public List<form_Validator> getForm_validators() {
        return form_validators;
    }

    public void addForm_validator(Form_validator form_validator) {
        this.form_validators.add(form_validator);
    }

}