





import java.util.List;
import java.util.ArrayList;

public class website_ContentUnit extends NamedDisplayElement {

    private String purposeSummary;
    private String captionClass;
    private boolean createDefaultUriElement;
    private String requiresRole;
    private boolean omitCaption;
    private String alternative;
    private String uriElement;





    private website_ActionMenuEntry website_actionmenuentry;


    public website_ContentUnit(
        String purposeSummary,        String captionClass,        boolean createDefaultUriElement,        String requiresRole,        boolean omitCaption,        String alternative,        String uriElement    ) {
        super(
        );
        this.purposeSummary = purposeSummary;
        this.captionClass = captionClass;
        this.createDefaultUriElement = createDefaultUriElement;
        this.requiresRole = requiresRole;
        this.omitCaption = omitCaption;
        this.alternative = alternative;
        this.uriElement = uriElement;
    }


    public String getPurposesummary() {
        return purposeSummary;
    }

    public void setPurposesummary(String purposeSummary) {
        this.purposeSummary = purposeSummary;
    }
    public String getCaptionclass() {
        return captionClass;
    }

    public void setCaptionclass(String captionClass) {
        this.captionClass = captionClass;
    }
    public boolean getCreatedefaulturielement() {
        return createDefaultUriElement;
    }

    public void setCreatedefaulturielement(boolean createDefaultUriElement) {
        this.createDefaultUriElement = createDefaultUriElement;
    }
    public String getRequiresrole() {
        return requiresRole;
    }

    public void setRequiresrole(String requiresRole) {
        this.requiresRole = requiresRole;
    }
    public boolean getOmitcaption() {
        return omitCaption;
    }

    public void setOmitcaption(boolean omitCaption) {
        this.omitCaption = omitCaption;
    }
    public String getAlternative() {
        return alternative;
    }

    public void setAlternative(String alternative) {
        this.alternative = alternative;
    }
    public String getUrielement() {
        return uriElement;
    }

    public void setUrielement(String uriElement) {
        this.uriElement = uriElement;
    }

    public website_ActionMenuEntry getWebsite_actionmenuentry() {
        return website_actionmenuentry;
    }

    public void setWebsite_actionmenuentry(website_ActionMenuEntry website_actionmenuentry) {
        this.website_actionmenuentry = website_actionmenuentry;
    }

}