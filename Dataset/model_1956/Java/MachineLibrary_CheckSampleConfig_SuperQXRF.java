





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_CheckSampleConfig_SuperQXRF  {

    private String program;
    private String anaProg;
    private int seq_X;
    private String samples;
    private String sampleID;
    private String minutes;





    private MachineLibrary_CheckSample_SuperQXRF machinelibrary_checksample_superqxrf;


    public MachineLibrary_CheckSampleConfig_SuperQXRF(
        String program,        String anaProg,        int seq_X,        String samples,        String sampleID,        String minutes    ) {
        this.program = program;
        this.anaProg = anaProg;
        this.seq_X = seq_X;
        this.samples = samples;
        this.sampleID = sampleID;
        this.minutes = minutes;
    }


    public String getProgram() {
        return program;
    }

    public void setProgram(String program) {
        this.program = program;
    }
    public String getAnaprog() {
        return anaProg;
    }

    public void setAnaprog(String anaProg) {
        this.anaProg = anaProg;
    }
    public int getSeq_x() {
        return seq_X;
    }

    public void setSeq_x(int seq_X) {
        this.seq_X = seq_X;
    }
    public String getSamples() {
        return samples;
    }

    public void setSamples(String samples) {
        this.samples = samples;
    }
    public String getSampleid() {
        return sampleID;
    }

    public void setSampleid(String sampleID) {
        this.sampleID = sampleID;
    }
    public String getMinutes() {
        return minutes;
    }

    public void setMinutes(String minutes) {
        this.minutes = minutes;
    }

    public MachineLibrary_CheckSample_SuperQXRF getMachinelibrary_checksample_superqxrf() {
        return machinelibrary_checksample_superqxrf;
    }

    public void setMachinelibrary_checksample_superqxrf(MachineLibrary_CheckSample_SuperQXRF machinelibrary_checksample_superqxrf) {
        this.machinelibrary_checksample_superqxrf = machinelibrary_checksample_superqxrf;
    }

}