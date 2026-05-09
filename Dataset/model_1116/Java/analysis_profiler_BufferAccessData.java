





import java.util.List;
import java.util.ArrayList;

public class analysis_profiler_BufferAccessData extends MemoryAccessData {

    private String sourcePort;
    private String targetActor;
    private String targetPort;
    private String sourceActor;



    public analysis_profiler_BufferAccessData(
        String sourcePort,        String targetActor,        String targetPort,        String sourceActor    ) {
        super(
        );
        this.sourcePort = sourcePort;
        this.targetActor = targetActor;
        this.targetPort = targetPort;
        this.sourceActor = sourceActor;
    }


    public String getSourceport() {
        return sourcePort;
    }

    public void setSourceport(String sourcePort) {
        this.sourcePort = sourcePort;
    }
    public String getTargetactor() {
        return targetActor;
    }

    public void setTargetactor(String targetActor) {
        this.targetActor = targetActor;
    }
    public String getTargetport() {
        return targetPort;
    }

    public void setTargetport(String targetPort) {
        this.targetPort = targetPort;
    }
    public String getSourceactor() {
        return sourceActor;
    }

    public void setSourceactor(String sourceActor) {
        this.sourceActor = sourceActor;
    }


}