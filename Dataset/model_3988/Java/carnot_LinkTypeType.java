





import java.util.List;
import java.util.ArrayList;

public class carnot_LinkTypeType extends IMetaType, IExtensibleElement {

    private String sourceCardinality;
    private String targetCardinality;
    private String targetClass;
    private String showLinkTypeName;
    private String sourceSymbol;
    private String sourceRole;
    private String targetRole;
    private String lineStyle;
    private String targetSymbol;
    private String lineColor;
    private String showRoleNames;
    private String sourceClass;





    private carnot_ModelType carnot_modeltype;


    public carnot_LinkTypeType(
        String sourceCardinality,        String targetCardinality,        String targetClass,        String showLinkTypeName,        String sourceSymbol,        String sourceRole,        String targetRole,        String lineStyle,        String targetSymbol,        String lineColor,        String showRoleNames,        String sourceClass    ) {
        super(
        );
        this.sourceCardinality = sourceCardinality;
        this.targetCardinality = targetCardinality;
        this.targetClass = targetClass;
        this.showLinkTypeName = showLinkTypeName;
        this.sourceSymbol = sourceSymbol;
        this.sourceRole = sourceRole;
        this.targetRole = targetRole;
        this.lineStyle = lineStyle;
        this.targetSymbol = targetSymbol;
        this.lineColor = lineColor;
        this.showRoleNames = showRoleNames;
        this.sourceClass = sourceClass;
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
    public String getTargetclass() {
        return targetClass;
    }

    public void setTargetclass(String targetClass) {
        this.targetClass = targetClass;
    }
    public String getShowlinktypename() {
        return showLinkTypeName;
    }

    public void setShowlinktypename(String showLinkTypeName) {
        this.showLinkTypeName = showLinkTypeName;
    }
    public String getSourcesymbol() {
        return sourceSymbol;
    }

    public void setSourcesymbol(String sourceSymbol) {
        this.sourceSymbol = sourceSymbol;
    }
    public String getSourcerole() {
        return sourceRole;
    }

    public void setSourcerole(String sourceRole) {
        this.sourceRole = sourceRole;
    }
    public String getTargetrole() {
        return targetRole;
    }

    public void setTargetrole(String targetRole) {
        this.targetRole = targetRole;
    }
    public String getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(String lineStyle) {
        this.lineStyle = lineStyle;
    }
    public String getTargetsymbol() {
        return targetSymbol;
    }

    public void setTargetsymbol(String targetSymbol) {
        this.targetSymbol = targetSymbol;
    }
    public String getLinecolor() {
        return lineColor;
    }

    public void setLinecolor(String lineColor) {
        this.lineColor = lineColor;
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

    public carnot_ModelType getCarnot_modeltype() {
        return carnot_modeltype;
    }

    public void setCarnot_modeltype(carnot_ModelType carnot_modeltype) {
        this.carnot_modeltype = carnot_modeltype;
    }

}