





import java.util.List;
import java.util.ArrayList;

public class ansic_declaration_specifiers  {

    private String function_specifier;
    private String storage_class_specifier;





    private ansic_declaration_specifiers ansic_declaration_specifiers;


    public ansic_declaration_specifiers(
        String function_specifier,        String storage_class_specifier    ) {
        this.function_specifier = function_specifier;
        this.storage_class_specifier = storage_class_specifier;
    }


    public String getFunction_specifier() {
        return function_specifier;
    }

    public void setFunction_specifier(String function_specifier) {
        this.function_specifier = function_specifier;
    }
    public String getStorage_class_specifier() {
        return storage_class_specifier;
    }

    public void setStorage_class_specifier(String storage_class_specifier) {
        this.storage_class_specifier = storage_class_specifier;
    }

    public ansic_declaration_specifiers getAnsic_declaration_specifiers() {
        return ansic_declaration_specifiers;
    }

    public void setAnsic_declaration_specifiers(ansic_declaration_specifiers ansic_declaration_specifiers) {
        this.ansic_declaration_specifiers = ansic_declaration_specifiers;
    }

}