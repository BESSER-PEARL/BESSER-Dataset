





import java.util.List;
import java.util.ArrayList;

public class simulink_msglib_LinkLayer extends Block {

    private int sourceBufferSize;
    private boolean bufferOverflowPossible;
    private int messageLossProbability;
    private int bufferSize;
    private String messageMapping;
    private String delayMin;
    private String delayMax;
    private boolean messageRetransmission;



    public simulink_msglib_LinkLayer(
        int sourceBufferSize,        boolean bufferOverflowPossible,        int messageLossProbability,        int bufferSize,        String messageMapping,        String delayMin,        String delayMax,        boolean messageRetransmission    ) {
        super(
        );
        this.sourceBufferSize = sourceBufferSize;
        this.bufferOverflowPossible = bufferOverflowPossible;
        this.messageLossProbability = messageLossProbability;
        this.bufferSize = bufferSize;
        this.messageMapping = messageMapping;
        this.delayMin = delayMin;
        this.delayMax = delayMax;
        this.messageRetransmission = messageRetransmission;
    }


    public int getSourcebuffersize() {
        return sourceBufferSize;
    }

    public void setSourcebuffersize(int sourceBufferSize) {
        this.sourceBufferSize = sourceBufferSize;
    }
    public boolean getBufferoverflowpossible() {
        return bufferOverflowPossible;
    }

    public void setBufferoverflowpossible(boolean bufferOverflowPossible) {
        this.bufferOverflowPossible = bufferOverflowPossible;
    }
    public int getMessagelossprobability() {
        return messageLossProbability;
    }

    public void setMessagelossprobability(int messageLossProbability) {
        this.messageLossProbability = messageLossProbability;
    }
    public int getBuffersize() {
        return bufferSize;
    }

    public void setBuffersize(int bufferSize) {
        this.bufferSize = bufferSize;
    }
    public String getMessagemapping() {
        return messageMapping;
    }

    public void setMessagemapping(String messageMapping) {
        this.messageMapping = messageMapping;
    }
    public String getDelaymin() {
        return delayMin;
    }

    public void setDelaymin(String delayMin) {
        this.delayMin = delayMin;
    }
    public String getDelaymax() {
        return delayMax;
    }

    public void setDelaymax(String delayMax) {
        this.delayMax = delayMax;
    }
    public boolean getMessageretransmission() {
        return messageRetransmission;
    }

    public void setMessageretransmission(boolean messageRetransmission) {
        this.messageRetransmission = messageRetransmission;
    }


}