





import java.util.List;
import java.util.ArrayList;

public class website_DynamicUnit extends ContentUnit {

    private String footer;
    private String errorClass;
    private String controlClass;
    private String header;
    private String footerClass;
    private String headerClass;





    private List<website_UnitSupportAction> website_unitsupportactions;




    private website_UnitField website_unitfield;




    private List<website_UnitField> website_unitfields;




    private List<website_EntityOrView> website_entityorviews;


    public website_DynamicUnit(
        String footer,        String errorClass,        String controlClass,        String header,        String footerClass,        String headerClass    ) {
        super(
        );
        this.footer = footer;
        this.errorClass = errorClass;
        this.controlClass = controlClass;
        this.header = header;
        this.footerClass = footerClass;
        this.headerClass = headerClass;
        this.website_unitsupportactions = new ArrayList<>();
        this.website_unitfields = new ArrayList<>();
        this.website_entityorviews = new ArrayList<>();
    }

    public website_DynamicUnit(
        String footer,        String errorClass,        String controlClass,        String header,        String footerClass,        String headerClass        ArrayList<website_UnitSupportAction> website_unitsupportactions,        ArrayList<website_UnitField> website_unitfields,        ArrayList<website_EntityOrView> website_entityorviews    ) {
        this.footer = footer;
        this.errorClass = errorClass;
        this.controlClass = controlClass;
        this.header = header;
        this.footerClass = footerClass;
        this.headerClass = headerClass;
        this.website_unitsupportactions = website_unitsupportactions;
        this.website_unitfields = website_unitfields;
        this.website_entityorviews = website_entityorviews;
    }

    public String getFooter() {
        return footer;
    }

    public void setFooter(String footer) {
        this.footer = footer;
    }
    public String getErrorclass() {
        return errorClass;
    }

    public void setErrorclass(String errorClass) {
        this.errorClass = errorClass;
    }
    public String getControlclass() {
        return controlClass;
    }

    public void setControlclass(String controlClass) {
        this.controlClass = controlClass;
    }
    public String getHeader() {
        return header;
    }

    public void setHeader(String header) {
        this.header = header;
    }
    public String getFooterclass() {
        return footerClass;
    }

    public void setFooterclass(String footerClass) {
        this.footerClass = footerClass;
    }
    public String getHeaderclass() {
        return headerClass;
    }

    public void setHeaderclass(String headerClass) {
        this.headerClass = headerClass;
    }

    public List<website_UnitSupportAction> getWebsite_unitsupportactions() {
        return website_unitsupportactions;
    }

    public void addWebsite_unitsupportaction(Website_unitsupportaction website_unitsupportaction) {
        this.website_unitsupportactions.add(website_unitsupportaction);
    }
    public website_UnitField getWebsite_unitfield() {
        return website_unitfield;
    }

    public void setWebsite_unitfield(website_UnitField website_unitfield) {
        this.website_unitfield = website_unitfield;
    }
    public List<website_UnitField> getWebsite_unitfields() {
        return website_unitfields;
    }

    public void addWebsite_unitfield(Website_unitfield website_unitfield) {
        this.website_unitfields.add(website_unitfield);
    }
    public List<website_EntityOrView> getWebsite_entityorviews() {
        return website_entityorviews;
    }

    public void addWebsite_entityorview(Website_entityorview website_entityorview) {
        this.website_entityorviews.add(website_entityorview);
    }

}