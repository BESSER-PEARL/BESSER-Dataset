





import java.util.List;
import java.util.ArrayList;

public class carnot_LinkTypeType extends IMetaType, IExtensibleElement {

    private String sourceSymbol;
    private String targetClass;
    private String targetSymbol;
    private String lineStyle;
    private String targetRole;
    private String targetCardinality;
    private String sourceClass;
    private String sourceCardinality;
    private String showLinkTypeName;
    private String sourceRole;
    private String lineColor;
    private String showRoleNames;





    private carnot_ModelType carnot_modeltype;


    public carnot_LinkTypeType(
        String sourceSymbol,        String targetClass,        String targetSymbol,        String lineStyle,        String targetRole,        String targetCardinality,        String sourceClass,        String sourceCardinality,        String showLinkTypeName,        String sourceRole,        String lineColor,        String showRoleNames    ) {
        super(
        );
        this.sourceSymbol = sourceSymbol;
        this.targetClass = targetClass;
        this.targetSymbol = targetSymbol;
        this.lineStyle = lineStyle;
        this.targetRole = targetRole;
        this.targetCardinality = targetCardinality;
        this.sourceClass = sourceClass;
        this.sourceCardinality = sourceCardinality;
        this.showLinkTypeName = showLinkTypeName;
        this.sourceRole = sourceRole;
        this.lineColor = lineColor;
        this.showRoleNames = showRoleNames;
    }


    public String getSourcesymbol() {
        return sourceSymbol;
    }

    public void setSourcesymbol(String sourceSymbol) {
        this.sourceSymbol = sourceSymbol;
    }
    public String getTargetclass() {
        return targetClass;
    }

    public void setTargetclass(String targetClass) {
        this.targetClass = targetClass;
    }
    public String getTargetsymbol() {
        return targetSymbol;
    }

    public void setTargetsymbol(String targetSymbol) {
        this.targetSymbol = targetSymbol;
    }
    public String getLinestyle() {
        return lineStyle;
    }

    public void setLinestyle(String lineStyle) {
        this.lineStyle = lineStyle;
    }
    public String getTargetrole() {
        return targetRole;
    }

    public void setTargetrole(String targetRole) {
        this.targetRole = targetRole;
    }
    public String getTargetcardinality() {
        return targetCardinality;
    }

    public void setTargetcardinality(String targetCardinality) {
        this.targetCardinality = targetCardinality;
    }
    public String getSourceclass() {
        return sourceClass;
    }

    public void setSourceclass(String sourceClass) {
        this.sourceClass = sourceClass;
    }
    public String getSourcecardinality() {
        return sourceCardinality;
    }

    public void setSourcecardinality(String sourceCardinality) {
        this.sourceCardinality = sourceCardinality;
    }
    public String getShowlinktypename() {
        return showLinkTypeName;
    }

    public void setShowlinktypename(String showLinkTypeName) {
        this.showLinkTypeName = showLinkTypeName;
    }
    public String getSourcerole() {
        return sourceRole;
    }

    public void setSourcerole(String sourceRole) {
        this.sourceRole = sourceRole;
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

    public carnot_ModelType getCarnot_modeltype() {
        return carnot_modeltype;
    }

    public void setCarnot_modeltype(carnot_ModelType carnot_modeltype) {
        this.carnot_modeltype = carnot_modeltype;
    }

}