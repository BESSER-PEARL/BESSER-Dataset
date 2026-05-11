





import java.util.List;
import java.util.ArrayList;

public class website_ParameterReference extends Path {

    private String name;





    private website_SelectionParameter website_selectionparameter;


    public website_ParameterReference(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public website_SelectionParameter getWebsite_selectionparameter() {
        return website_selectionparameter;
    }

    public void setWebsite_selectionparameter(website_SelectionParameter website_selectionparameter) {
        this.website_selectionparameter = website_selectionparameter;
    }

}