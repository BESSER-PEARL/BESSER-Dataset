





import java.util.List;
import java.util.ArrayList;

public class persistence_Association extends Feature {

    private String inputColumnClass;
    private int serializationMaxDepth;
    private String targetDisplayLabel;
    private String targetDisplayClass;
    private boolean pseudo;
    private String targetHeaderClass;
    private String pivotTableName;
    private String targetInputClass;
    private boolean targetPrimaryKey;
    private boolean unique;
    private String targetColumnName;
    private boolean bidirectional;
    private String targetFeatureName;
    private String inputElementClass;
    private String targetFooterClass;





    private persistence_Entity persistence_entity;




    private persistence_Entity persistence_entity;




    private persistence_Entity persistence_entity;




    private persistence_Entity persistence_entity;


    public persistence_Association(
        String inputColumnClass,        int serializationMaxDepth,        String targetDisplayLabel,        String targetDisplayClass,        boolean pseudo,        String targetHeaderClass,        String pivotTableName,        String targetInputClass,        boolean targetPrimaryKey,        boolean unique,        String targetColumnName,        boolean bidirectional,        String targetFeatureName,        String inputElementClass,        String targetFooterClass    ) {
        super(
        );
        this.inputColumnClass = inputColumnClass;
        this.serializationMaxDepth = serializationMaxDepth;
        this.targetDisplayLabel = targetDisplayLabel;
        this.targetDisplayClass = targetDisplayClass;
        this.pseudo = pseudo;
        this.targetHeaderClass = targetHeaderClass;
        this.pivotTableName = pivotTableName;
        this.targetInputClass = targetInputClass;
        this.targetPrimaryKey = targetPrimaryKey;
        this.unique = unique;
        this.targetColumnName = targetColumnName;
        this.bidirectional = bidirectional;
        this.targetFeatureName = targetFeatureName;
        this.inputElementClass = inputElementClass;
        this.targetFooterClass = targetFooterClass;
    }


    public String getInputcolumnclass() {
        return inputColumnClass;
    }

    public void setInputcolumnclass(String inputColumnClass) {
        this.inputColumnClass = inputColumnClass;
    }
    public int getSerializationmaxdepth() {
        return serializationMaxDepth;
    }

    public void setSerializationmaxdepth(int serializationMaxDepth) {
        this.serializationMaxDepth = serializationMaxDepth;
    }
    public String getTargetdisplaylabel() {
        return targetDisplayLabel;
    }

    public void setTargetdisplaylabel(String targetDisplayLabel) {
        this.targetDisplayLabel = targetDisplayLabel;
    }
    public String getTargetdisplayclass() {
        return targetDisplayClass;
    }

    public void setTargetdisplayclass(String targetDisplayClass) {
        this.targetDisplayClass = targetDisplayClass;
    }
    public boolean getPseudo() {
        return pseudo;
    }

    public void setPseudo(boolean pseudo) {
        this.pseudo = pseudo;
    }
    public String getTargetheaderclass() {
        return targetHeaderClass;
    }

    public void setTargetheaderclass(String targetHeaderClass) {
        this.targetHeaderClass = targetHeaderClass;
    }
    public String getPivottablename() {
        return pivotTableName;
    }

    public void setPivottablename(String pivotTableName) {
        this.pivotTableName = pivotTableName;
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
    public String getInputelementclass() {
        return inputElementClass;
    }

    public void setInputelementclass(String inputElementClass) {
        this.inputElementClass = inputElementClass;
    }
    public String getTargetfooterclass() {
        return targetFooterClass;
    }

    public void setTargetfooterclass(String targetFooterClass) {
        this.targetFooterClass = targetFooterClass;
    }

    public persistence_Entity getPersistence_entity() {
        return persistence_entity;
    }

    public void setPersistence_entity(persistence_Entity persistence_entity) {
        this.persistence_entity = persistence_entity;
    }
    public persistence_Entity getPersistence_entity() {
        return persistence_entity;
    }

    public void setPersistence_entity(persistence_Entity persistence_entity) {
        this.persistence_entity = persistence_entity;
    }
    public persistence_Entity getPersistence_entity() {
        return persistence_entity;
    }

    public void setPersistence_entity(persistence_Entity persistence_entity) {
        this.persistence_entity = persistence_entity;
    }
    public persistence_Entity getPersistence_entity() {
        return persistence_entity;
    }

    public void setPersistence_entity(persistence_Entity persistence_entity) {
        this.persistence_entity = persistence_entity;
    }

}