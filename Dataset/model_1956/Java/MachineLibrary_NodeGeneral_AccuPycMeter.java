





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_NodeGeneral_AccuPycMeter  {

    private int sendSampleWeight;
    private int expectSampleWeight;
    private int runTimout;
    private int polling;





    private MachineLibrary_NodeGeneralSpecial machinelibrary_nodegeneralspecial;


    public MachineLibrary_NodeGeneral_AccuPycMeter(
        int sendSampleWeight,        int expectSampleWeight,        int runTimout,        int polling    ) {
        this.sendSampleWeight = sendSampleWeight;
        this.expectSampleWeight = expectSampleWeight;
        this.runTimout = runTimout;
        this.polling = polling;
    }


    public int getSendsampleweight() {
        return sendSampleWeight;
    }

    public void setSendsampleweight(int sendSampleWeight) {
        this.sendSampleWeight = sendSampleWeight;
    }
    public int getExpectsampleweight() {
        return expectSampleWeight;
    }

    public void setExpectsampleweight(int expectSampleWeight) {
        this.expectSampleWeight = expectSampleWeight;
    }
    public int getRuntimout() {
        return runTimout;
    }

    public void setRuntimout(int runTimout) {
        this.runTimout = runTimout;
    }
    public int getPolling() {
        return polling;
    }

    public void setPolling(int polling) {
        this.polling = polling;
    }

    public MachineLibrary_NodeGeneralSpecial getMachinelibrary_nodegeneralspecial() {
        return machinelibrary_nodegeneralspecial;
    }

    public void setMachinelibrary_nodegeneralspecial(MachineLibrary_NodeGeneralSpecial machinelibrary_nodegeneralspecial) {
        this.machinelibrary_nodegeneralspecial = machinelibrary_nodegeneralspecial;
    }

}