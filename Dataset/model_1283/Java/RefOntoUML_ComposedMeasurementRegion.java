





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_ComposedMeasurementRegion extends MeasurementRegion {






    private List<RefOntoUML_BasicMeasurementRegion> refontouml_basicmeasurementregions;


    public RefOntoUML_ComposedMeasurementRegion(
    ) {
        super(
        );
        this.refontouml_basicmeasurementregions = new ArrayList<>();
    }

    public RefOntoUML_ComposedMeasurementRegion(
        ArrayList<RefOntoUML_BasicMeasurementRegion> refontouml_basicmeasurementregions    ) {
        this.refontouml_basicmeasurementregions = refontouml_basicmeasurementregions;
    }


    public List<RefOntoUML_BasicMeasurementRegion> getRefontouml_basicmeasurementregions() {
        return refontouml_basicmeasurementregions;
    }

    public void addRefontouml_basicmeasurementregion(Refontouml_basicmeasurementregion refontouml_basicmeasurementregion) {
        this.refontouml_basicmeasurementregions.add(refontouml_basicmeasurementregion);
    }

}