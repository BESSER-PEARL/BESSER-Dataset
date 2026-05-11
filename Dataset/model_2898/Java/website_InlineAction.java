





import java.util.List;
import java.util.ArrayList;

public class website_InlineAction extends NamedDisplayElement {

    private boolean disable;
    private String requiresRole;
    private String footer;
    private String header;
    private String headerClass;
    private String footerClass;



    public website_InlineAction(
        boolean disable,        String requiresRole,        String footer,        String header,        String headerClass,        String footerClass    ) {
        super(
        );
        this.disable = disable;
        this.requiresRole = requiresRole;
        this.footer = footer;
        this.header = header;
        this.headerClass = headerClass;
        this.footerClass = footerClass;
    }


    public boolean getDisable() {
        return disable;
    }

    public void setDisable(boolean disable) {
        this.disable = disable;
    }
    public String getRequiresrole() {
        return requiresRole;
    }

    public void setRequiresrole(String requiresRole) {
        this.requiresRole = requiresRole;
    }
    public String getFooter() {
        return footer;
    }

    public void setFooter(String footer) {
        this.footer = footer;
    }
    public String getHeader() {
        return header;
    }

    public void setHeader(String header) {
        this.header = header;
    }
    public String getHeaderclass() {
        return headerClass;
    }

    public void setHeaderclass(String headerClass) {
        this.headerClass = headerClass;
    }
    public String getFooterclass() {
        return footerClass;
    }

    public void setFooterclass(String footerClass) {
        this.footerClass = footerClass;
    }


}