





import java.util.List;
import java.util.ArrayList;

public class website_EntityAssociation extends EntityFeature, Association {

    private String pivotTableName;
    private boolean bidirectional;
    private String targetFeatureName;
    private String targetDisplayClass;
    private String targetInputClass;
    private boolean targetPrimaryKey;
    private String targetHeaderClass;
    private String targetFooterClass;
    private String targetDisplayLabel;





    private website_ModelLabelAssociation website_modellabelassociation;


    public website_EntityAssociation(
        String pivotTableName,        boolean bidirectional,        String targetFeatureName,        String targetDisplayClass,        String targetInputClass,        boolean targetPrimaryKey,        String targetHeaderClass,        String targetFooterClass,        String targetDisplayLabel    ) {
        super(
        );
        this.pivotTableName = pivotTableName;
        this.bidirectional = bidirectional;
        this.targetFeatureName = targetFeatureName;
        this.targetDisplayClass = targetDisplayClass;
        this.targetInputClass = targetInputClass;
        this.targetPrimaryKey = targetPrimaryKey;
        this.targetHeaderClass = targetHeaderClass;
        this.targetFooterClass = targetFooterClass;
        this.targetDisplayLabel = targetDisplayLabel;
    }


    public String getPivottablename() {
        return pivotTableName;
    }

    public void setPivottablename(String pivotTableName) {
        this.pivotTableName = pivotTableName;
    }
    public boolean getBidirectional() {
        return bidirectional;
    }

    public void setBidirectional(boolean bidirectional) {
        this.bidirectional = bidirectional;
    }
    public String getTargetfeaturename() {
        return targetFeatureName;
    }

    public void setTargetfeaturename(String targetFeatureName) {
        this.targetFeatureName = targetFeatureName;
    }
    public String getTargetdisplayclass() {
        return targetDisplayClass;
    }

    public void setTargetdisplayclass(String targetDisplayClass) {
        this.targetDisplayClass = targetDisplayClass;
    }
    public String getTargetinputclass() {
        return targetInputClass;
    }

    public void setTargetinputclass(String targetInputClass) {
        this.targetInputClass = targetInputClass;
    }
    public boolean getTargetprimarykey() {
        return targetPrimaryKey;
    }

    public void setTargetprimarykey(boolean targetPrimaryKey) {
        this.targetPrimaryKey = targetPrimaryKey;
    }
    public String getTargetheaderclass() {
        return targetHeaderClass;
    }

    public void setTargetheaderclass(String targetHeaderClass) {
        this.targetHeaderClass = targetHeaderClass;
    }
    public String getTargetfooterclass() {
        return targetFooterClass;
    }

    public void setTargetfooterclass(String targetFooterClass) {
        this.targetFooterClass = targetFooterClass;
    }
    public String getTargetdisplaylabel() {
        return targetDisplayLabel;
    }

    public void setTargetdisplaylabel(String targetDisplayLabel) {
        this.targetDisplayLabel = targetDisplayLabel;
    }

    public website_ModelLabelAssociation getWebsite_modellabelassociation() {
        return website_modellabelassociation;
    }

    public void setWebsite_modellabelassociation(website_ModelLabelAssociation website_modellabelassociation) {
        this.website_modellabelassociation = website_modellabelassociation;
    }

}