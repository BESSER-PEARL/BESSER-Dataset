





import java.util.List;
import java.util.ArrayList;

public class website_Selection extends NamedElement {

    private boolean selected;
    private boolean distinct;
    private int limit;





    private website_SelectionParameter website_selectionparameter;




    private website_Service website_service;




    private website_Service website_service;




    private List<website_SelectionParameter> website_selectionparameters;


    public website_Selection(
        boolean selected,        boolean distinct,        int limit    ) {
        super(
        );
        this.selected = selected;
        this.distinct = distinct;
        this.limit = limit;
        this.website_selectionparameters = new ArrayList<>();
    }

    public website_Selection(
        boolean selected,        boolean distinct,        int limit        ArrayList<website_SelectionParameter> website_selectionparameters    ) {
        this.selected = selected;
        this.distinct = distinct;
        this.limit = limit;
        this.website_selectionparameters = website_selectionparameters;
    }

    public boolean getSelected() {
        return selected;
    }

    public void setSelected(boolean selected) {
        this.selected = selected;
    }
    public boolean getDistinct() {
        return distinct;
    }

    public void setDistinct(boolean distinct) {
        this.distinct = distinct;
    }
    public int getLimit() {
        return limit;
    }

    public void setLimit(int limit) {
        this.limit = limit;
    }

    public website_SelectionParameter getWebsite_selectionparameter() {
        return website_selectionparameter;
    }

    public void setWebsite_selectionparameter(website_SelectionParameter website_selectionparameter) {
        this.website_selectionparameter = website_selectionparameter;
    }
    public website_Service getWebsite_service() {
        return website_service;
    }

    public void setWebsite_service(website_Service website_service) {
        this.website_service = website_service;
    }
    public website_Service getWebsite_service() {
        return website_service;
    }

    public void setWebsite_service(website_Service website_service) {
        this.website_service = website_service;
    }
    public List<website_SelectionParameter> getWebsite_selectionparameters() {
        return website_selectionparameters;
    }

    public void addWebsite_selectionparameter(Website_selectionparameter website_selectionparameter) {
        this.website_selectionparameters.add(website_selectionparameter);
    }

}