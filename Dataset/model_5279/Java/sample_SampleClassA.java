





import java.util.List;
import java.util.ArrayList;

public class sample_SampleClassA extends SampleClassInterface {

    private String sampleAttribute;





    private sample_SampleClassC sample_sampleclassc;


    public sample_SampleClassA(
        String sampleAttribute    ) {
        super(
        );
        this.sampleAttribute = sampleAttribute;
    }


    public String getSampleattribute() {
        return sampleAttribute;
    }

    public void setSampleattribute(String sampleAttribute) {
        this.sampleAttribute = sampleAttribute;
    }

    public sample_SampleClassC getSample_sampleclassc() {
        return sample_sampleclassc;
    }

    public void setSample_sampleclassc(sample_SampleClassC sample_sampleclassc) {
        this.sample_sampleclassc = sample_sampleclassc;
    }

}