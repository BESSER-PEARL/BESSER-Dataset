





import java.util.List;
import java.util.ArrayList;

public class aml_Drive extends SuperEntity {






    private aml_SpeedFeature aml_speedfeature;




    private aml_FormFeature aml_formfeature;


    public aml_Drive(
    ) {
        super(
        );
    }



    public aml_SpeedFeature getAml_speedfeature() {
        return aml_speedfeature;
    }

    public void setAml_speedfeature(aml_SpeedFeature aml_speedfeature) {
        this.aml_speedfeature = aml_speedfeature;
    }
    public aml_FormFeature getAml_formfeature() {
        return aml_formfeature;
    }

    public void setAml_formfeature(aml_FormFeature aml_formfeature) {
        this.aml_formfeature = aml_formfeature;
    }

}