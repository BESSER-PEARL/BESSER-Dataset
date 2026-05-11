





import java.util.List;
import java.util.ArrayList;

public class carnot_LinkTypeType extends IExtensibleElement, IMetaType {

    private String showLinkTypeName;
    private String targetSymbol;
    private String sourceCardinality;
    private String targetCardinality;
    private String targetRole;
    private String showRoleNames;
    private String sourceClass;
    private String sourceRole;
    private String lineStyle;
    private String targetClass;
    private String lineColor;
    private String sourceSymbol;





    private carnot_ModelType carnot_modeltype;


    public carnot_LinkTypeType(
        String showLinkTypeName,        String targetSymbol,        String sourceCardinality,        String targetCardinality,        String targetRole,        String showRoleNames,        String sourceClass,        String sourceRole,        String lineStyle,        String targetClass,        String lineColor,        String sourceSymbol    ) {
        super(
        );
        this.showLinkTypeName = showLinkTypeName;
        this.targetSymbol = targetSymbol;
        this.sourceCardinality = sourceCardinality;
        this.targetCardinality = targetCardinality;
        this.targetRole = targetRole;
        this.showRoleNames = showRoleNames;
        this.sourceClass = sourceClass;
        this.sourceRole = sourceRole;
        this.lineStyle = lineStyle;
        this.targetClass = targetClass;
        this.lineColor = lineColor;
        this.sourceSymbol = sourceSymbol;
    }


    public String getShowlinktypename() {
        return showLinkTypeName;
    }

    public void setShowlinktypename(String showLinkTypeName) {
        this.showLinkTypeName = showLinkTypeName;
    }
    public String getTargetsymbol() {
        return targetSymbol;
    }

    public void setTargetsymbol(String targetSymbol) {
        this.targetSymbol = targetSymbol;
    }
    public String getSourcecardinality() {
        return sourceCardinality;
    }

    public void setSourcecardinality(String sourceCardinality) {
        this.sourceCardinality = sourceCardinality;
    }
    public String getTargetcardinality() {
        return targetCardinality;
    }

    public void setTargetcardinality(String targetCardinality) {
        this.targetCardinality = targetCardinality;
    }
    public String getTargetrole() {
        return targetRole;
    }

    public void setTargetrole(String targetRole) {
        this.targetRole = targetRole;
    }
    public String getShowrolenames() {
        return showRoleNames;
    }

    public void setShowrolenames(String showRoleNames) {
        this.showRoleNames = showRoleNames;
    }
    public String getSourceclass() {
        return sourceClass;
    }

    public void setSourceclass(String sourceClass) {
        this.sourceClass = sourceClass;
    }
    public String getSourcerole() {
        return sourceRole;
    }

    public void setSourcerole(String sourceRole) {
        this.sourceRole = sourceRole;
    }
    public String getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(String lineStyle) {
        this.lineStyle = lineStyle;
    }
    public String getTargetclass() {
        return targetClass;
    }

    public void setTargetclass(String targetClass) {
        this.targetClass = targetClass;
    }
    public String getLinecolor() {
        return lineColor;
    }

    public void setLinecolor(String lineColor) {
        this.lineColor = lineColor;
    }
    public String getSourcesymbol() {
        return sourceSymbol;
    }

    public void setSourcesymbol(String sourceSymbol) {
        this.sourceSymbol = sourceSymbol;
    }

    public carnot_ModelType getCarnot_modeltype() {
        return carnot_modeltype;
    }

    public void setCarnot_modeltype(carnot_ModelType carnot_modeltype) {
        this.carnot_modeltype = carnot_modeltype;
    }

}