





import java.util.List;
import java.util.ArrayList;

public class persistence_EntityAssociation extends EntityFeature, Association {

    private boolean bidirectional;
    private String targetFooterClass;
    private String targetHeaderClass;
    private boolean targetPrimaryKey;
    private String targetDisplayClass;
    private String targetDisplayLabel;
    private String targetInputClass;
    private String targetFeatureName;
    private String pivotTableName;





    private persistence_ModelLabelAssociation persistence_modellabelassociation;


    public persistence_EntityAssociation(
        boolean bidirectional,        String targetFooterClass,        String targetHeaderClass,        boolean targetPrimaryKey,        String targetDisplayClass,        String targetDisplayLabel,        String targetInputClass,        String targetFeatureName,        String pivotTableName    ) {
        super(
        );
        this.bidirectional = bidirectional;
        this.targetFooterClass = targetFooterClass;
        this.targetHeaderClass = targetHeaderClass;
        this.targetPrimaryKey = targetPrimaryKey;
        this.targetDisplayClass = targetDisplayClass;
        this.targetDisplayLabel = targetDisplayLabel;
        this.targetInputClass = targetInputClass;
        this.targetFeatureName = targetFeatureName;
        this.pivotTableName = pivotTableName;
    }


    public boolean getBidirectional() {
        return bidirectional;
    }

    public void setBidirectional(boolean bidirectional) {
        this.bidirectional = bidirectional;
    }
    public String getTargetfooterclass() {
        return targetFooterClass;
    }

    public void setTargetfooterclass(String targetFooterClass) {
        this.targetFooterClass = targetFooterClass;
    }
    public String getTargetheaderclass() {
        return targetHeaderClass;
    }

    public void setTargetheaderclass(String targetHeaderClass) {
        this.targetHeaderClass = targetHeaderClass;
    }
    public boolean getTargetprimarykey() {
        return targetPrimaryKey;
    }

    public void setTargetprimarykey(boolean targetPrimaryKey) {
        this.targetPrimaryKey = targetPrimaryKey;
    }
    public String getTargetdisplayclass() {
        return targetDisplayClass;
    }

    public void setTargetdisplayclass(String targetDisplayClass) {
        this.targetDisplayClass = targetDisplayClass;
    }
    public String getTargetdisplaylabel() {
        return targetDisplayLabel;
    }

    public void setTargetdisplaylabel(String targetDisplayLabel) {
        this.targetDisplayLabel = targetDisplayLabel;
    }
    public String getTargetinputclass() {
        return targetInputClass;
    }

    public void setTargetinputclass(String targetInputClass) {
        this.targetInputClass = targetInputClass;
    }
    public String getTargetfeaturename() {
        return targetFeatureName;
    }

    public void setTargetfeaturename(String targetFeatureName) {
        this.targetFeatureName = targetFeatureName;
    }
    public String getPivottablename() {
        return pivotTableName;
    }

    public void setPivottablename(String pivotTableName) {
        this.pivotTableName = pivotTableName;
    }

    public persistence_ModelLabelAssociation getPersistence_modellabelassociation() {
        return persistence_modellabelassociation;
    }

    public void setPersistence_modellabelassociation(persistence_ModelLabelAssociation persistence_modellabelassociation) {
        this.persistence_modellabelassociation = persistence_modellabelassociation;
    }

}