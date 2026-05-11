





import java.util.List;
import java.util.ArrayList;

public class website_UnitFeature extends InlineActionContainer, UnitField {

    private boolean autofocus;
    private boolean onlyDisplayWhenNotEmpty;
    private String footer;
    private String inputClass;
    private String displayClass;
    private String nullDisplayValue;
    private boolean required;
    private String footerClass;
    private String displayLabel;
    private String headerClass;





    private website_Expression website_expression;


    public website_UnitFeature(
        boolean autofocus,        boolean onlyDisplayWhenNotEmpty,        String footer,        String inputClass,        String displayClass,        String nullDisplayValue,        boolean required,        String footerClass,        String displayLabel,        String headerClass    ) {
        super(
        );
        this.autofocus = autofocus;
        this.onlyDisplayWhenNotEmpty = onlyDisplayWhenNotEmpty;
        this.footer = footer;
        this.inputClass = inputClass;
        this.displayClass = displayClass;
        this.nullDisplayValue = nullDisplayValue;
        this.required = required;
        this.footerClass = footerClass;
        this.displayLabel = displayLabel;
        this.headerClass = headerClass;
    }


    public boolean getAutofocus() {
        return autofocus;
    }

    public void setAutofocus(boolean autofocus) {
        this.autofocus = autofocus;
    }
    public boolean getOnlydisplaywhennotempty() {
        return onlyDisplayWhenNotEmpty;
    }

    public void setOnlydisplaywhennotempty(boolean onlyDisplayWhenNotEmpty) {
        this.onlyDisplayWhenNotEmpty = onlyDisplayWhenNotEmpty;
    }
    public String getFooter() {
        return footer;
    }

    public void setFooter(String footer) {
        this.footer = footer;
    }
    public String getInputclass() {
        return inputClass;
    }

    public void setInputclass(String inputClass) {
        this.inputClass = inputClass;
    }
    public String getDisplayclass() {
        return displayClass;
    }

    public void setDisplayclass(String displayClass) {
        this.displayClass = displayClass;
    }
    public String getNulldisplayvalue() {
        return nullDisplayValue;
    }

    public void setNulldisplayvalue(String nullDisplayValue) {
        this.nullDisplayValue = nullDisplayValue;
    }
    public boolean getRequired() {
        return required;
    }

    public void setRequired(boolean required) {
        this.required = required;
    }
    public String getFooterclass() {
        return footerClass;
    }

    public void setFooterclass(String footerClass) {
        this.footerClass = footerClass;
    }
    public String getDisplaylabel() {
        return displayLabel;
    }

    public void setDisplaylabel(String displayLabel) {
        this.displayLabel = displayLabel;
    }
    public String getHeaderclass() {
        return headerClass;
    }

    public void setHeaderclass(String headerClass) {
        this.headerClass = headerClass;
    }

    public website_Expression getWebsite_expression() {
        return website_expression;
    }

    public void setWebsite_expression(website_Expression website_expression) {
        this.website_expression = website_expression;
    }

}