





import java.util.List;
import java.util.ArrayList;

public class website_FilterParameter extends NamedElement {

    private String defaultValue;
    private String placeholder;





    private website_SelectionParameter website_selectionparameter;


    public website_FilterParameter(
        String defaultValue,        String placeholder    ) {
        super(
        );
        this.defaultValue = defaultValue;
        this.placeholder = placeholder;
    }


    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public String getPlaceholder() {
        return placeholder;
    }

    public void setPlaceholder(String placeholder) {
        this.placeholder = placeholder;
    }

    public website_SelectionParameter getWebsite_selectionparameter() {
        return website_selectionparameter;
    }

    public void setWebsite_selectionparameter(website_SelectionParameter website_selectionparameter) {
        this.website_selectionparameter = website_selectionparameter;
    }

}