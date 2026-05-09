





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_HistoryConfig_AccuPyc  {

    private String currentSample;
    private float sampleCupWeight;
    private String currentSampleID;





    private MachineLibrary_History_AccuPycMeter machinelibrary_history_accupycmeter;


    public MachineLibrary_HistoryConfig_AccuPyc(
        String currentSample,        float sampleCupWeight,        String currentSampleID    ) {
        this.currentSample = currentSample;
        this.sampleCupWeight = sampleCupWeight;
        this.currentSampleID = currentSampleID;
    }


    public String getCurrentsample() {
        return currentSample;
    }

    public void setCurrentsample(String currentSample) {
        this.currentSample = currentSample;
    }
    public float getSamplecupweight() {
        return sampleCupWeight;
    }

    public void setSamplecupweight(float sampleCupWeight) {
        this.sampleCupWeight = sampleCupWeight;
    }
    public String getCurrentsampleid() {
        return currentSampleID;
    }

    public void setCurrentsampleid(String currentSampleID) {
        this.currentSampleID = currentSampleID;
    }

    public MachineLibrary_History_AccuPycMeter getMachinelibrary_history_accupycmeter() {
        return machinelibrary_history_accupycmeter;
    }

    public void setMachinelibrary_history_accupycmeter(MachineLibrary_History_AccuPycMeter machinelibrary_history_accupycmeter) {
        this.machinelibrary_history_accupycmeter = machinelibrary_history_accupycmeter;
    }

}