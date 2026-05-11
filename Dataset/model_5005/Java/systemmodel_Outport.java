





import java.util.List;
import java.util.ArrayList;

public class systemmodel_Outport extends Port {






    private systemmodel_Block systemmodel_block;




    private List<systemmodel_Signal> systemmodel_signals;




    private systemmodel_Block systemmodel_block;




    private systemmodel_Signal systemmodel_signal;


    public systemmodel_Outport(
    ) {
        super(
        );
        this.systemmodel_signals = new ArrayList<>();
    }

    public systemmodel_Outport(
        ArrayList<systemmodel_Signal> systemmodel_signals    ) {
        this.systemmodel_signals = systemmodel_signals;
    }


    public systemmodel_Block getSystemmodel_block() {
        return systemmodel_block;
    }

    public void setSystemmodel_block(systemmodel_Block systemmodel_block) {
        this.systemmodel_block = systemmodel_block;
    }
    public List<systemmodel_Signal> getSystemmodel_signals() {
        return systemmodel_signals;
    }

    public void addSystemmodel_signal(Systemmodel_signal systemmodel_signal) {
        this.systemmodel_signals.add(systemmodel_signal);
    }
    public systemmodel_Block getSystemmodel_block() {
        return systemmodel_block;
    }

    public void setSystemmodel_block(systemmodel_Block systemmodel_block) {
        this.systemmodel_block = systemmodel_block;
    }
    public systemmodel_Signal getSystemmodel_signal() {
        return systemmodel_signal;
    }

    public void setSystemmodel_signal(systemmodel_Signal systemmodel_signal) {
        this.systemmodel_signal = systemmodel_signal;
    }

}