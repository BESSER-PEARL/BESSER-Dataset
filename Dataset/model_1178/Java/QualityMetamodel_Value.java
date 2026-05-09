





import java.util.List;
import java.util.ArrayList;

public class QualityMetamodel_Value extends VariableDeclaration {

    private String description;





    private QualityMetamodel_Operation qualitymetamodel_operation;




    private QualityMetamodel_ValueType qualitymetamodel_valuetype;




    private QualityMetamodel_QualityModel qualitymetamodel_qualitymodel;




    private QualityMetamodel_QualityAttribute qualitymetamodel_qualityattribute;




    private QualityMetamodel_ValueType qualitymetamodel_valuetype;


    public QualityMetamodel_Value(
        String description    ) {
        super(
        );
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public QualityMetamodel_Operation getQualitymetamodel_operation() {
        return qualitymetamodel_operation;
    }

    public void setQualitymetamodel_operation(QualityMetamodel_Operation qualitymetamodel_operation) {
        this.qualitymetamodel_operation = qualitymetamodel_operation;
    }
    public QualityMetamodel_ValueType getQualitymetamodel_valuetype() {
        return qualitymetamodel_valuetype;
    }

    public void setQualitymetamodel_valuetype(QualityMetamodel_ValueType qualitymetamodel_valuetype) {
        this.qualitymetamodel_valuetype = qualitymetamodel_valuetype;
    }
    public QualityMetamodel_QualityModel getQualitymetamodel_qualitymodel() {
        return qualitymetamodel_qualitymodel;
    }

    public void setQualitymetamodel_qualitymodel(QualityMetamodel_QualityModel qualitymetamodel_qualitymodel) {
        this.qualitymetamodel_qualitymodel = qualitymetamodel_qualitymodel;
    }
    public QualityMetamodel_QualityAttribute getQualitymetamodel_qualityattribute() {
        return qualitymetamodel_qualityattribute;
    }

    public void setQualitymetamodel_qualityattribute(QualityMetamodel_QualityAttribute qualitymetamodel_qualityattribute) {
        this.qualitymetamodel_qualityattribute = qualitymetamodel_qualityattribute;
    }
    public QualityMetamodel_ValueType getQualitymetamodel_valuetype() {
        return qualitymetamodel_valuetype;
    }

    public void setQualitymetamodel_valuetype(QualityMetamodel_ValueType qualitymetamodel_valuetype) {
        this.qualitymetamodel_valuetype = qualitymetamodel_valuetype;
    }

}