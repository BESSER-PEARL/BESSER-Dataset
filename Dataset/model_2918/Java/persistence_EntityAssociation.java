





import java.util.List;
import java.util.ArrayList;

public class persistence_EntityAssociation extends EntityFeature, Association {

    private boolean bidirectional;
    private String targetFeatureName;
    private String targetDisplayClass;
    private String targetFooterClass;
    private String targetHeaderClass;
    private boolean targetPrimaryKey;
    private String targetInputClass;
    private String pivotTableName;
    private boolean unique;
    private String targetColumnName;
    private String targetDisplayLabel;





    private persistence_ModelLabelAssociation persistence_modellabelassociation;


    public persistence_EntityAssociation(
        boolean bidirectional,        String targetFeatureName,        String targetDisplayClass,        String targetFooterClass,        String targetHeaderClass,        boolean targetPrimaryKey,        String targetInputClass,        String pivotTableName,        boolean unique,        String targetColumnName,        String targetDisplayLabel    ) {
        super(
        );
        this.bidirectional = bidirectional;
        this.targetFeatureName = targetFeatureName;
        this.targetDisplayClass = targetDisplayClass;
        this.targetFooterClass = targetFooterClass;
        this.targetHeaderClass = targetHeaderClass;
        this.targetPrimaryKey = targetPrimaryKey;
        this.targetInputClass = targetInputClass;
        this.pivotTableName = pivotTableName;
        this.unique = unique;
        this.targetColumnName = targetColumnName;
        this.targetDisplayLabel = targetDisplayLabel;
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
    public String getTargetinputclass() {
        return targetInputClass;
    }

    public void setTargetinputclass(String targetInputClass) {
        this.targetInputClass = targetInputClass;
    }
    public String getPivottablename() {
        return pivotTableName;
    }

    public void setPivottablename(String pivotTableName) {
        this.pivotTableName = pivotTableName;
    }
    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public String getTargetcolumnname() {
        return targetColumnName;
    }

    public void setTargetcolumnname(String targetColumnName) {
        this.targetColumnName = targetColumnName;
    }
    public String getTargetdisplaylabel() {
        return targetDisplayLabel;
    }

    public void setTargetdisplaylabel(String targetDisplayLabel) {
        this.targetDisplayLabel = targetDisplayLabel;
    }

    public persistence_ModelLabelAssociation getPersistence_modellabelassociation() {
        return persistence_modellabelassociation;
    }

    public void setPersistence_modellabelassociation(persistence_ModelLabelAssociation persistence_modellabelassociation) {
        this.persistence_modellabelassociation = persistence_modellabelassociation;
    }

}