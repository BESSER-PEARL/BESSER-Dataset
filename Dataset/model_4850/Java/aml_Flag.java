





import java.util.List;
import java.util.ArrayList;

public class aml_Flag  {

    private String description;
    private String label;
    private String flagType;





    private aml_Annotation aml_annotation;




    private aml_Witness aml_witness;


    public aml_Flag(
        String description,        String label,        String flagType    ) {
        this.description = description;
        this.label = label;
        this.flagType = flagType;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getFlagtype() {
        return flagType;
    }

    public void setFlagtype(String flagType) {
        this.flagType = flagType;
    }

    public aml_Annotation getAml_annotation() {
        return aml_annotation;
    }

    public void setAml_annotation(aml_Annotation aml_annotation) {
        this.aml_annotation = aml_annotation;
    }
    public aml_Witness getAml_witness() {
        return aml_witness;
    }

    public void setAml_witness(aml_Witness aml_witness) {
        this.aml_witness = aml_witness;
    }

}