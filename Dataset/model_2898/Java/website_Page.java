





import java.util.List;
import java.util.ArrayList;

public class website_Page extends NamedDisplayElement, UnitContainer {

    private String uriElement;
    private String styleClass;
    private boolean authenticated;
    private String navigationLabel;
    private String topMenuOption;
    private int topMenuRank;





    private website_WebGenModel website_webgenmodel;


    public website_Page(
        String uriElement,        String styleClass,        boolean authenticated,        String navigationLabel,        String topMenuOption,        int topMenuRank    ) {
        super(
        );
        this.uriElement = uriElement;
        this.styleClass = styleClass;
        this.authenticated = authenticated;
        this.navigationLabel = navigationLabel;
        this.topMenuOption = topMenuOption;
        this.topMenuRank = topMenuRank;
    }


    public String getUrielement() {
        return uriElement;
    }

    public void setUrielement(String uriElement) {
        this.uriElement = uriElement;
    }
    public String getStyleclass() {
        return styleClass;
    }

    public void setStyleclass(String styleClass) {
        this.styleClass = styleClass;
    }
    public boolean getAuthenticated() {
        return authenticated;
    }

    public void setAuthenticated(boolean authenticated) {
        this.authenticated = authenticated;
    }
    public String getNavigationlabel() {
        return navigationLabel;
    }

    public void setNavigationlabel(String navigationLabel) {
        this.navigationLabel = navigationLabel;
    }
    public String getTopmenuoption() {
        return topMenuOption;
    }

    public void setTopmenuoption(String topMenuOption) {
        this.topMenuOption = topMenuOption;
    }
    public int getTopmenurank() {
        return topMenuRank;
    }

    public void setTopmenurank(int topMenuRank) {
        this.topMenuRank = topMenuRank;
    }

    public website_WebGenModel getWebsite_webgenmodel() {
        return website_webgenmodel;
    }

    public void setWebsite_webgenmodel(website_WebGenModel website_webgenmodel) {
        this.website_webgenmodel = website_webgenmodel;
    }

}