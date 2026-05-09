





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_MeasurementDomain extends MeasurementStructure {






    private RefOntoUML_MeasurementDimension refontouml_measurementdimension;




    private RefOntoUML_Expression refontouml_expression;




    private List<RefOntoUML_MeasurementDimension> refontouml_measurementdimensions;


    public RefOntoUML_MeasurementDomain(
    ) {
        super(
        );
        this.refontouml_measurementdimensions = new ArrayList<>();
    }

    public RefOntoUML_MeasurementDomain(
        ArrayList<RefOntoUML_MeasurementDimension> refontouml_measurementdimensions    ) {
        this.refontouml_measurementdimensions = refontouml_measurementdimensions;
    }


    public RefOntoUML_MeasurementDimension getRefontouml_measurementdimension() {
        return refontouml_measurementdimension;
    }

    public void setRefontouml_measurementdimension(RefOntoUML_MeasurementDimension refontouml_measurementdimension) {
        this.refontouml_measurementdimension = refontouml_measurementdimension;
    }
    public RefOntoUML_Expression getRefontouml_expression() {
        return refontouml_expression;
    }

    public void setRefontouml_expression(RefOntoUML_Expression refontouml_expression) {
        this.refontouml_expression = refontouml_expression;
    }
    public List<RefOntoUML_MeasurementDimension> getRefontouml_measurementdimensions() {
        return refontouml_measurementdimensions;
    }

    public void addRefontouml_measurementdimension(Refontouml_measurementdimension refontouml_measurementdimension) {
        this.refontouml_measurementdimensions.add(refontouml_measurementdimension);
    }

}