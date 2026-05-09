





import java.util.List;
import java.util.ArrayList;

public class domain_DropDownSelection extends OptionSelection {

    private String initialOptionValue;





    private domain_Selection domain_selection;




    private domain_Context domain_context;


    public domain_DropDownSelection(
        String initialOptionValue    ) {
        super(
        );
        this.initialOptionValue = initialOptionValue;
    }


    public String getInitialoptionvalue() {
        return initialOptionValue;
    }

    public void setInitialoptionvalue(String initialOptionValue) {
        this.initialOptionValue = initialOptionValue;
    }

    public domain_Selection getDomain_selection() {
        return domain_selection;
    }

    public void setDomain_selection(domain_Selection domain_selection) {
        this.domain_selection = domain_selection;
    }
    public domain_Context getDomain_context() {
        return domain_context;
    }

    public void setDomain_context(domain_Context domain_context) {
        this.domain_context = domain_context;
    }

}